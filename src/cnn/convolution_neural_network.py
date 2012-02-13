#!/usr/bin/env python2.7

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from argparse import ArgumentParser
import logging
import sys

import numpy
from scipy.stats import pearsonr
import theano
import theano.tensor as T
from theano.sandbox.cuda.basic_ops import gpu_from_host
from least_squares_regression import TheanoLeastSquaresRegression
from utils import *

class ConvPoolLayer(object):
    def __init__(self, rng, x_data, image_shape, filter_shape, poolsize):
        assert image_shape[1]==filter_shape[1]
        self.W = theano.shared(numpy.zeros(filter_shape,
            dtype=theano.config.floatX))
        self.b = theano.shared(numpy.zeros((filter_shape[0],),
            dtype=theano.config.floatX))
        fil_in = numpy.prod(filter_shape[1:])
        fil_out = filter_shape[0] * numpy.prod(filter_shape[2:]) / \
                    numpy.prod(poolsize)
        W_bound = numpy.sqrt(6 / (fil_in + fil_out))
        self.W.set_value(numpy.asarray(rng.uniform(low=-W_bound, high=W_bound,
            size=filter_shape), dtype=theano.config.floatX), borrow=True)
        conv_out = T.nnet.conv.conv2d(x_data, self.W,
                filter_shape=filter_shape, image_shape=image_shape)
        pooled_out = T.signal.downsample.max_pool_2d(conv_out, ds=poolsize,
                ignore_border=True)
        self.output = T.tanh(pooled_out + self.b.dimshuffle('x', 0, 'x', 'x'))
        self.params = [self.W, self.b]

def train_cnn(data_file_name, reg_lambda=0.01, learning_rate=0.001, display=True):
    train_data, test_data = load_images(data_file_name)
    n_training_examples, n_features = train_data[0].shape
    real_scores = test_data[1].T.tolist()


    train_data = to_theano_shared(train_data)
    test_data = to_theano_shared(test_data)

    rng = numpy.random.RandomState(1234)
    x = T.matrix('x')
    y = T.vector('y')

    layer_0_input = x.reshape((n_training_examples, 1, 128, 128))
    layer_0 = ConvPoolLayer(rng=rng, x_data=layer_0_input,
            image_shape=(n_training_examples, 1, 128, 128), filter_shape=(48, 1,
                9, 9), poolsize=(8,8))
    layer_1_input = layer_0.output.flatten(2)
    layer_1 = TheanoLeastSquaresRegression(layer_1_input.T, 15*15*48,
            n_training_examples)

    cost = layer_1.cost(y) 

    test_model =theano.function([],
            outputs=[cost, layer_1.y_pred],
            givens={x:test_data[0][:], y:test_data[1][:]})

    params = layer_0.params + layer_1.params
    g_params = []
    for param in params:
        g_param = T.grad(cost, param)
        g_params.append(g_param)

    updates = {}

    for param, g_param in zip(params, g_params):
        updates[param] = param - learning_rate * g_param

    train_model = theano.function([],
            outputs=cost, updates=updates,
            givens={x:train_data[0][:], y:train_data[1][:]})

    current_cost = numpy.asarray(train_model())
    logging.info('initial cost %f' % current_cost)
    old_cost = 0
    iterations = 0
    logging.info('beginning stochastic gradient descent')
    while ((abs(current_cost- old_cost)) > 0.0001):
        old_cost = current_cost
        current_cost = numpy.asarray(train_model())
        if iterations % 10 == 0:
            logging.info('iteration % 9d cost % 9f' % (iterations, current_cost))
        iterations += 1

    error, predictions = test_model()

    # Print the results
    logging.info('training cost minimised: %f' % current_cost)
    logging.info('test error: %f' % error)
    
    predictions = predictions[0].tolist()
    logging.debug('predictions %s', str(predictions))
    pearsons = pearsonr(real_scores, predictions)
    logging.info('pearsons correlation: %f, %f' % pearsons)
    # Save our weights should we ever need them again
    plot_correlation(real_scores, predictions, 'cnn','yoyyo', show=True)


def build_argument_parser():
    argument_parser = ArgumentParser()
    argument_parser.add_argument('--data-file-name', nargs='+', 
                                  default=[DEFAULT_DATA_FILE_NAME])
    argument_parser.add_argument('--n-neurons-per-layer', default=100, type=int)
    argument_parser.add_argument('--learning-rate', type=float,
                                 default=0.01)
    argument_parser.add_argument('--reg-lambda', type=float, default=0.1)
    argument_parser.add_argument('--log-level', default='INFO')
    argument_parser.add_argument('--display', action='store_true')
    return argument_parser

def main(argv=None):
    if argv is None:
        argv = sys.argv 
    argument_parser = build_argument_parser()
    args = argument_parser.parse_args(args=argv[1:])
    numeric_level = getattr(logging, args.log_level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % loglevel)
    logging.basicConfig(format='%(levelname)s: %(asctime)s: %(message)s',
                        level=numeric_level)
    for data_file_name in args.data_file_name:
        train_cnn(data_file_name, 
                    learning_rate=args.learning_rate, 
                    display=args.display)
    
if __name__ == '__main__':
    exit(main())

