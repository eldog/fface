#!/usr/bin/env python2.7

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from argparse import ArgumentParser
import gc
import logging
import sys
import time

import numpy
from scipy.stats import pearsonr
import theano
import theano.tensor as T
from theano.sandbox.cuda.basic_ops import gpu_from_host
from least_squares_regression import TheanoLeastSquaresRegression
from neural_net_eig_faces import HiddenLayer
from utils import *

VERSION = 'v0.0'
REG_LAMBDA_1 = 0.00
REG_LAMBDA_2 = 0.01
LEARNING_RATE = 0.0001
BATCH_SIZE = 25
N_EPOCHS = 1000
N_HIDDEN_UNITS = 500

class ConvPoolLayer(object):
    """
    A layer of a neural network that performs a convolutions followed by a
    maxpool on its input.
    """
    def __init__(self, rng, x_data, image_shape, filter_shape, pool_size):
        """
        Initialize the weights of the filters randomly
        
        type: numpy.random.RandomState
        parameter: rng: A random number generator from which the weights will be
                        initialised.
        
        type: theano.tensor
        parameter: x_data: The input data to learn from

        type: 4-tuple or 4 element list
        parameter: image_shape: (batch size, number of feature maps, image
                                height, image width)

        type: 4-tuple or 4 element list
        parameter: filter_shape: (number of filters, number of feature
                                  maps, filter height, filter width)

        type: 2-tuple or 2 element list
        parameter: pool_size: (maxpool height, maxpool width)
        """
        # Check number of feature maps is equal in both
        assert image_shape[1]==filter_shape[1]
        self.W = theano.shared(numpy.zeros(filter_shape,
                                           dtype=theano.config.floatX))
        self.b = theano.shared(numpy.zeros((filter_shape[0],),
                                           dtype=theano.config.floatX))
        fil_in = numpy.prod(filter_shape[1:])
        fil_out = filter_shape[0] * numpy.prod(filter_shape[2:]) \
                  / numpy.prod(pool_size)
        W_bound = numpy.sqrt(6. / (fil_in + fil_out))
        self.W.set_value(numpy.asarray(rng.uniform(low=-W_bound, 
                                                   high=W_bound,
                                                   size=filter_shape), 
                                       dtype=theano.config.floatX), 
                         borrow=True)
        conv_out = T.nnet.conv.conv2d(x_data, 
                                     self.W,
                                     filter_shape=filter_shape,
                                     image_shape=image_shape)
        pooled_out = T.signal.downsample.max_pool_2d(conv_out, 
                                                     ds=pool_size,
                                                     ignore_border=True)
        self.output = T.tanh(pooled_out + self.b.dimshuffle('x', 0, 'x', 'x'))
        self.params = [self.W, self.b]

    def __get_state__(self):
        return (self.W, self.b)

    def __set_state__(self, state):
        W, b = state
        self.W = W
        self.b = b

class SingleLayerConvNN(object):
    """
    A single layered convolution neural attempting to recreate the Single Layer
    Model from [Gray10] http://www.dbs.ifi.lmu.de/~yu_k/dgray_eccv2010final.pdf
    """
    def __init__(self, rng, x_data, batch_size, image_shape, filter_shape, 
                 pool_size):
        """
        Build the model

        type: numpy.random.RandomState
        parameter: rng: A random number generator from which the weights will be
                        initialised.
        
        type: theano.tensor
        parameter: x_data: The input data to learn from

        type: 4-tuple or 4 element list
        parameter: image_shape: (batch size, number of feature maps, image
                                height, image width)

        type: 4-tuple or 4 element list
        parameter: filter_shape: (number of filters, number of feature
                                  maps, filter height, filter width)

        type: 2-tuple or 2 element list
        parameter: pool_size: (maxpool height, maxpool width)
        """
        self.layer_0_input = x_data.reshape(image_shape)
        self.layer_0 = ConvPoolLayer(rng=rng, 
                                     x_data=self.layer_0_input,
                                     image_shape=image_shape, 
                                     filter_shape=filter_shape, 
                                     pool_size=pool_size)
        self.regression_input = self.layer_0.output.flatten(2)
        output_size = calculate_output_size(image_shape, 
                                            filter_shape,
                                            pool_size)
        self.regression = TheanoLeastSquaresRegression(self.regression_input.T, 
                                                    output_size,
                                                    batch_size)
        self.l1 = abs(self.layer_0.W).sum() + abs(self.regression.theta).sum()
        self.l2 = (self.layer_0.W ** 2).sum() + (self.regression.theta ** 2).sum()
        self.params = self.layer_0.params + self.regression.params

class TwoLayerConvNN(object):
    def __init__(self, rng, x_data, batch_size, image_shape, filter_shape,
                 pool_size):
        self.layer_0_input = x_data.reshape(image_shape)
        self.layer_0 = ConvPoolLayer(rng=rng, 
                                     x_data=self.layer_0_input,
                                     image_shape=image_shape, 
                                     filter_shape=filter_shape, 
                                     pool_size=pool_size)
        layer_1_image_shape = (batch_size, 
                               filter_shape[0], 
                               (image_shape[2] - filter_shape[2] + 1) \
                                // pool_size[0],
                               (image_shape[3] - filter_shape[3] + 1) \
                                // pool_size[1])
        layer_1_filter_shape = (48, filter_shape[0], 5, 5)
        layer_1_pool_size = (2,2)
        self.layer_1 = ConvPoolLayer(rng=rng, 
                                   x_data=self.layer_0.output, 
                                   image_shape=layer_1_image_shape,
                                    filter_shape=layer_1_filter_shape,
                                    pool_size=layer_1_pool_size)
        
        self.layer_1_input = self.layer_1.output.flatten(2)
        output_size_1 = calculate_output_size(layer_1_image_shape, 
                                              layer_1_filter_shape,
                                              layer_1_pool_size)
        self.regression = TheanoLeastSquaresRegression(self.layer_1_input.T, 
                                                       output_size_1, 
                                                       batch_size)
        self.l1 = abs(self.layer_0.W).sum() + abs(self.layer_1.W).sum() + abs(self.regression.theta).sum()
        self.l2 = (self.regression.theta ** 2).sum() + (self.layer_0.W ** 2).sum() + (self.layer_1.W ** 2).sum() 
        self.params = self.layer_0.params + self.layer_1.params + self.regression.params
        

def calculate_output_size(image_shape, filter_shape, pool_size):
    return ((image_shape[2] - filter_shape[2] + 1) / pool_size[0]) \
            *((image_shape[3] - filter_shape[3] + 1) / pool_size[1]) \
            * filter_shape[0]

def train_cnn(data_file_name, batch_size=BATCH_SIZE, reg_lambda_1=REG_LAMBDA_1, 
              reg_lambda_2=REG_LAMBDA_2, learning_rate=LEARNING_RATE,
              n_epochs=N_EPOCHS, n_hidden_units=N_HIDDEN_UNITS, display=True):
    train_data, validation_data, test_data, test_data_file_names = load_images(data_file_name)
    # get our data to fit our batch size
    train_data = trim_to_batch_size(train_data, batch_size)
    validation_data = trim_to_batch_size(validation_data, batch_size)
    test_data = trim_to_batch_size(test_data, batch_size)
    test_data_file_names = test_data_file_names[:len(test_data[0])]
    # Get the information from our shape before it becomes a shared variable 
    n_training_examples, n_channels, n_features = train_data[0].shape
    n_validation_examples = validation_data[0].shape[0]
    n_testing_examples = test_data[0].shape[0]
    #err

    means, ranges = get_means_and_ranges(train_data[0])
    train_data[0] = normalize_zero_mean(train_data[0], means, ranges)
    test_data[0] = normalize_zero_mean(test_data[0], means, ranges)
    validation_data[0] = normalize_zero_mean(validation_data[0], means, ranges)

    real_scores = test_data[1].T.tolist()
    real_val_scores = validation_data[1].T.tolist()
    # Turn our data into shared variables so we can make good use of the GPU 
    train_data_x, train_data_y  = to_theano_shared(train_data)
    test_data_x, test_data_y = to_theano_shared(test_data)
    validation_data_x, validation_data_y = to_theano_shared(validation_data)
    logging.info('data has been prepared')

    n_training_batches = n_training_examples // batch_size
    n_validation_batches = n_validation_examples // batch_size
    n_testing_batches = n_testing_examples // batch_size
    logging.debug('using %d training batches' % n_training_batches)
    logging.debug('using %d validation batches' % n_validation_batches)
    logging.debug('using %d testing batches' % n_testing_batches)

    rng = numpy.random.RandomState(1234)
    x = T.tensor3('x')
    y = T.vector('y')
    index = T.lscalar('index')

    cnn = SingleLayerConvNN(rng, 
                            x, 
                            batch_size, 
                            image_shape=(batch_size, 3, 128, 128),
                            filter_shape=(48, 3, 9, 9),
                            pool_size=(8,8))

    cost = cnn.regression.cost(y) + reg_lambda_2 * cnn.l2

    test_givens = {
                    x:test_data_x[index*batch_size : (index+1)*batch_size],
                    y:test_data_y[index*batch_size : (index+1)*batch_size]
                  }
    test_model = theano.function([index],
                                 outputs=[cost, cnn.regression.y_pred],
                                 givens=test_givens)

    validation_givens = {
                    x:validation_data_x[index*batch_size : (index+1)*batch_size],
                    y:validation_data_y[index*batch_size : (index+1)*batch_size]
                        }
    validate_model = theano.function([index],
                                       outputs=[cost, cnn.regression.y_pred],
                                       givens=validation_givens)

    g_params = []
    for param in cnn.params:
        g_param = T.grad(cost, param)
        g_params.append(g_param)
    updates = {}
    for param, g_param in zip(cnn.params, g_params):
        updates[param] = param - learning_rate * g_param
    train_givens = {
                    x:train_data_x[index*batch_size : (index+1)*batch_size],
                    y:train_data_y[index*batch_size : (index+1)*batch_size]
                   }
    train_model = theano.function([index],
                                  outputs=cost, 
                                  updates=updates,
                                  givens=train_givens)

    start_time = time.clock()
    current_cost = numpy.inf
    logging.info('initial cost %f' % current_cost)
    
    old_cost = 0
    epochs = 1
    done_looping = False
    logging.info('beginning stochastic gradient descent')

    patience = 5000
    patience_increase = 2
    improvement_threshold = 0.995
    validation_frequency = min(n_training_batches, patience / 2)
    # For inspecting out error during the descent
    best_validation_so_far = numpy.inf
    best_iter = 0
    test_score = 0.0
    costs_train = []
    costs_validations = []
    costs_tests = []
    costs_pearsons = []
    while (epochs < n_epochs) and (not done_looping):
        old_cost = current_cost
        sum_cost = 0
        for batch_index in xrange(n_training_batches):
            iteration = epochs * n_training_batches + batch_index
            _cost = numpy.asarray(train_model(batch_index))
            costs_train.append((iteration, _cost))
            if (iteration + 1) % validation_frequency == 0:
                sum_errors = 0
                predictions = []
                for i in xrange(n_validation_batches):
                    error, next_predictions = validate_model(i)
                    predictions += next_predictions[0].tolist()
                    sum_errors += error
                validation_cost = sum_errors / n_validation_batches
                costs_validations.append((iteration, validation_cost))
                pearsons = pearsonr(real_val_scores, predictions)
                logging.info('current validation cost at epoch %d iter %d is %f pearsons %f' 
                             % (epochs, iteration, validation_cost, pearsons[0]))
                if validation_cost < best_validation_so_far:
                    best_validation_so_far = validation_cost
                    best_iter = iteration

                    if validation_cost < best_validation_so_far * improvement_threshold:
                        patience = max(patience, iteration * patience_increase)
                    sum_errors = 0
                    predictions = []
                    for test_index in  xrange(n_testing_batches):
                        error, next_predictions = test_model(test_index)
                        predictions += next_predictions[0].tolist()
                        sum_errors += error
                    test_score = sum_errors / n_testing_batches
                    costs_tests.append((iteration, test_score))
                    pearsons = pearsonr(real_scores, predictions)
                    costs_pearsons.append((iteration, pearsons[0]))
                    logging.info('test error %f pearsons %f' % (test_score, pearsons[0]))
            sum_cost += _cost
            if patience <= iteration:
                done_looping = True
                break

        current_cost = sum_cost / n_training_batches
        logging.info('epoch % 5d patience %d error % 9f' % (epochs, patience, current_cost))
        epochs += 1

    end_time = time.clock()
    
    save_pickle((cnn.params), append_timestamp_to_file_name('cnn-%s' % VERSION))
    logging.info('training cost minimised at: %f' % current_cost)
    logging.info('testing model')
    predictions = []
    sum_errors = 0
    for batch_index in  xrange(n_testing_batches):
        error, next_predictions = test_model(batch_index)
        predictions += next_predictions[0].tolist()
        sum_errors += error

    # Print the results
    logging.info('mean test error: %f' % (sum_errors / n_testing_batches))
    logging.debug('predictions %s', str(predictions))
    pearsons = pearsonr(real_scores, predictions)
    logging.info('pearsons correlation: %f, %f' % pearsons)
    # Save our weights should we ever need them again
    logging.info('optimisation complete in %f minutes' 
                 % ((end_time - start_time) / 60))
    plot_correlation(real_scores, 
                     predictions,
                     test_data_file_names,
                     'cnn with pearsons %f and lambda %f'
                     % (pearsons[0], reg_lambda_2),
                     'cnn', 
                     show=True)
    plot_cost((zip(*costs_train)),
              (zip(*costs_validations)),
              (zip(*costs_tests)),
              (zip(*costs_pearsons)),
              'cnn with pearsons %f and batch size %d' 
              % (pearsons[0], batch_size))

def build_argument_parser():
    argument_parser = ArgumentParser()
    argument_parser.add_argument('--data-file-name', 
                                 nargs='+', 
                                 default=[DEFAULT_DATA_FILE_NAME])
    argument_parser.add_argument('--batch-size',
                                 type=int,
                                 default=BATCH_SIZE)
    argument_parser.add_argument('--learning-rate', 
                                 type=float,
                                 default=LEARNING_RATE)
    argument_parser.add_argument('--reg-lambda-1',
                                 type=float,
                                 default=REG_LAMBDA_1)
    argument_parser.add_argument('--reg-lambda-2', 
                                 type=float, 
                                 default=REG_LAMBDA_2)
    argument_parser.add_argument('--n-epochs',
                                 type=int,
                                 default=N_EPOCHS)
    argument_parser.add_argument('--n-hidden-units',
                                 type=int,
                                 default=N_HIDDEN_UNITS)
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
                  batch_size=args.batch_size,
                  learning_rate=args.learning_rate,
                  reg_lambda_1=args.reg_lambda_1,
                  reg_lambda_2=args.reg_lambda_2,
                  n_epochs=args.n_epochs,
                  n_hidden_units=args.n_hidden_units,
                  display=args.display)
    
if __name__ == '__main__':
    exit(main())

