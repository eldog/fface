#!/usr/bin/env python2.7

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import cPickle
import datetime
import logging
import os
import sys

from argparse import ArgumentParser

import Image
from matplotlib import cm, pyplot
from mpl_toolkits.mplot3d import Axes3D
import numpy
from scipy.stats import pearsonr
import theano
from theano import tensor as T

from eigenface import EigenFace
from least_squares_regression import TheanoLeastSquaresRegression
from utils import DEFAULT_DATA_FILE_NAME, load_images, to_theano_shared

image_dir = os.path.join(os.path.dirname(__file__),
                         '../../../img/')

def append_timestamp_to_file_name(file_name):
    d_time = datetime.datetime.utcnow().strftime('%H:%M:%S-%d-%m-%Y')
    return ('%s-%s' % (file_name, d_time))

def plot_correlation(x_data, theta, bias, y_data, data_file_name,
                     display=False):
    data_file_name = os.path.basename(data_file_name)
    x_guess = (numpy.dot(theta.T, x_data) + bias).T
    pyplot.plot(y_data, x_guess,'ro')
    pyplot.axis([-4, 4, -4, 4])
    pyplot.xlabel('human score')
    pyplot.ylabel('machine score')
    x = x_guess.T.tolist()
    y = y_data.tolist()
    y = map(float, y)
    pearsons = pearsonr(x[0],y) 
    logging.info('pearsons coefficient: %f' % pearsons[0])
    pyplot.title("Scatter of scores on data set %s with pearsons correlation %f"
                 % (data_file_name, pearsons[0]), fontsize='small')
    if display:
        pyplot.show()
    figure_file_name = os.path.join(image_dir, 
                                    '%s.png' % 
                                    append_timestamp_to_file_name('figure-%s' %
                                                              data_file_name))
    logging.info('writing scatterplot of results to %s' % figure_file_name)
    with open(figure_file_name, 'w') as figure_file:
        pyplot.savefig(figure_file, format='png')

def prepend_ones(data):
    return numpy.concatenate((numpy.ones((1, (data.shape[1])), 
                                dtype=theano.config.floatX), data))


def eigface_sgd(data_file_name, n_eigs=100, learning_rate=0.000000000000000001, 
                reg_lambda=0.1, display=False):
    train_data, test_data = load_images(data_file_name)
    eig_face = EigenFace(train_data[0], n_eigs=n_eigs)
    train_data[0] = eig_face.project_to_face_space(train_data[0])
    test_data[0] = eig_face.project_to_face_space(test_data[0])
    n_features, n_training_examples = train_data[0].shape
    n_features += 1 # we're going to add the ones on
    n_test_examples = test_data[0].shape[1]
    train_data[0] = prepend_ones(train_data[0])
    test_data[0] = prepend_ones(test_data[0])
    train_data = to_theano_shared(train_data)
    test_data = to_theano_shared(test_data)

    x_train, y_train = train_data
    x_test, y_test = test_data

    x = T.matrix('x')
    y = T.vector('y')

    tlsr = TheanoLeastSquaresRegression(x, n_features, n_training_examples,
                                        reg_lambda=reg_lambda)
    cost = tlsr.cost(y)
    test_model = theano.function([], outputs=cost, givens={x:x_test[:],
        y:y_test[:]})
    
    g_theta = T.grad(cost, tlsr.theta)
    g_bias = T.grad(cost, tlsr.bias)
    updates = {
                tlsr.theta : tlsr.theta - learning_rate * g_theta,
                tlsr.bias : tlsr.bias - learning_rate * g_bias
              }
    train_model = theano.function([], outputs=cost, updates=updates,
            givens={x:x_train[:], y:y_train[:]})

    current_cost = train_model()
    logging.info('initial cost %f' % current_cost)
    old_cost = 0
    iterations = 0
    logging.info('beginning stochastic gradient descent')
    while ((abs(current_cost- old_cost)) > 0.000001):
        old_cost = current_cost
        current_cost = train_model()
        if iterations % 1000 == 0:
            logging.info('iteration % 9d cost % 9f' % (iterations, current_cost))
        iterations += 1

    error = test_model()
    theta = tlsr.theta.get_value()
    bias = tlsr.theta.get_value()

    # Print the results
    logging.info('training cost minimised: %f' % current_cost)
    logging.info('test error: %f' % error)

    # Save our weights should we ever need them again
    theta_file_name = '%s.pickle' % append_timestamp_to_file_name('weights')
    logging.info('writing weights to %s' % theta_file_name)
    with open(theta_file_name, 'w') as out_file:
        cPickle.dump((theta, bias), out_file)

    plot_correlation(x_test.get_value(), theta, bias, y_test.get_value(),
                     data_file_name, display=display)

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
        eigface_sgd(data_file_name, n_eigs=args.n_eigs, 
                    learning_rate=args.learning_rate, 
                    reg_lambda=args.reg_lambda, display=args.display)
    
if __name__ == '__main__':
    sys.exit(main())
