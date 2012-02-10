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

from eigenface import EigenFace
from least_squares_regression import TheanoLeastSquaresRegression
from utils import *

class HiddenLayer(object):
    def __init__(self, rng, x_data, n_in, n_out, activation=T.tanh):
        self.W = theano.shared(
                value=(numpy.asarray(rng.uniform(low=-numpy.sqrt(6/(n_in+n_out)),
                high=numpy.sqrt(6/(n_in+n_out)),size=(n_in, n_out)),
                dtype=theano.config.floatX)), name='W')
        self.b = theano.shared(value=numpy.zeros((n_out,),
            dtype=theano.config.floatX), name='b')
        self.output = activation(T.dot(x_data, self.W) + self.b)
        self.params = [self.W, self.b]

class MLP(object):
    def __init__(self, rng, x_data, n_in, n_hidden, m):
        self.hidden_layer = HiddenLayer(rng, x_data, n_in, n_hidden)
        self.linear_regression = TheanoLeastSquaresRegression(
                                    self.hidden_layer.output.T, n_hidden, m)
        self.cost = self.linear_regression.cost
        self.params = self.hidden_layer.params + self.linear_regression.params
        self.output = self.linear_regression.y_pred
        self.L2_sqr = (self.hidden_layer.W ** 2).sum() \
                       + (self.linear_regression.theta ** 2).sum()
def prepend_ones(data):
    return numpy.concatenate((numpy.ones((1, (data.shape[1])), 
                                dtype=theano.config.floatX), data))

def train_nn(data_file_name, reg_lambda=0.01, learning_rate=0.01, n_eigs=11, 
        n_hidden=5000, display=True):
    train_data, test_data = load_images(data_file_name)
    eig_face = EigenFace.from_file(train_data[0], data_file_name, n_eigs)
    train_data[0] = get_face_space(data_file_name, 'train_x', train_data[0],
                                   eig_face)
    test_data[0] = get_face_space(data_file_name, 'test_x', test_data[0],
                                  eig_face)
    n_features, n_training_examples = train_data[0].shape
    #n_features += 1
    real_scores = test_data[1].T.tolist()
    #train_data[0] = prepend_ones(train_data[0])
    #test_data[0] = prepend_ones(test_data[0])

    train_data = to_theano_shared(train_data)
    test_data = to_theano_shared(test_data)

    rng = numpy.random.RandomState(1234)
    x = T.matrix('x')
    y = T.vector('y')

    mlp = MLP(rng, x, n_features, n_hidden, n_training_examples)
    cost = mlp.cost(y) + reg_lambda * mlp.L2_sqr

    test_model =theano.function([], outputs=[cost, mlp.output],
            givens={x:test_data[0][:], y:test_data[1][:]})

    g_params = []
    for param in mlp.params:
        g_param = T.grad(cost, param)
        g_params.append(g_param)

    updates = {}

    for param, g_param in zip(mlp.params, g_params):
        updates[param] = param - learning_rate * g_param

    train_model = theano.function([], outputs=cost, updates=updates,
            givens={x:train_data[0][:], y:train_data[1][:]})

    current_cost = train_model()
    logging.info('initial cost %f' % current_cost)
    old_cost = 0
    iterations = 0
    logging.info('beginning stochastic gradient descent')
    while ((abs(current_cost- old_cost)) > 0.000001):
        old_cost = current_cost
        current_cost = train_model()
        if iterations % 10 == 0:
            logging.info('iteration % 9d cost % 9f' % (iterations, current_cost))
        iterations += 1

    error, predictions = test_model()

    # Print the results
    logging.info('training cost minimised: %f' % current_cost)
    logging.info('test error: %f' % error)
    
    predictions = predictions[0].tolist()
    pearsons = pearsonr(real_scores, predictions)
    logging.info('pearsons correlation: %f, %f' % pearsons)
    # Save our weights should we ever need them again
    plot_correlation(real_scores, predictions, 'heya',
            'filename', show=True)

def build_argument_parser():
    argument_parser = ArgumentParser()
    argument_parser.add_argument('--data-file-name', nargs='+', 
                                  default=[DEFAULT_DATA_FILE_NAME])
    argument_parser.add_argument('--n-eigs', type=int, default=100)
    argument_parser.add_argument('--learning-rate', type=float,
                                 default=0.000000000000000001)
    argument_parser.add_argument('--reg-lambda', type=float, default=0.1)
    argument_parser.add_argument('--log-level', default='INFO')
    argument_parser.add_argument('--display')
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
        train_nn(data_file_name, n_eigs=args.n_eigs, 
                    learning_rate=args.learning_rate, 
                    reg_lambda=args.reg_lambda, display=args.display)
    
if __name__ == '__main__':
    exit(main())

