#!/usr/bin/env python2.7
"""
This experiment is designed to test gradient descent using Theano.

It uses the stanford ML course's housing price dataset available at
http://openclassroom.stanford.edu/MainFolder/courses/MachineLearning/exercises/ex3materials/ex3Data.zip

"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from argparse import ArgumentParser
import csv
import numpy
import sys

import theano
import theano.tensor as T

class LinearRegression(object):
    """
    Performs linear regression on a set of inputs
    """
    def __init__(self, _input, n_in, n_out):
        """
        Initialise the weights and bias and define the prediction function
        """
        self.theta = theano.shared(numpy.zeros((n_in),
                                           dtype=theano.config.floatX),
                                           name='theta')
        self.y_pred = T.dot(_input, self.theta)
        self.params = self.theta

    def squared_error(self, y):
        return T.mean(T.sqr(y - self.y_pred)) * 0.5


def load_data(data_file_name):
    """
    Load the data assuming the label is the last on the row
    :type data_file_name: str
    :param data_file_name: the name of the file containing data
    
    """
    data = numpy.genfromtxt(data_file_name, dtype=int, delimiter=',')
    features = data[:, :-1]
    labels = data[:, -1]
    def shared_data_set(data_x, data_y):
        shared_x = theano.shared(numpy.array(data_x,
                                             dtype=theano.config.floatX))
        shared_y = theano.shared(numpy.array(data_y,
                                             dtype=theano.config.floatX))
        return shared_x, shared_y
    middle = len(data) / 2
    t = numpy.concatenate((numpy.ones((middle,1)),features[:middle]), axis=1)
    train_x, train_y = shared_data_set(t, labels[:middle])
    test_x, test_y = shared_data_set(features[middle:], labels[middle:])
    return ((train_x, train_y), (test_x, test_y))

def stochastic_gradient_descent(data_file_name, learning_rate=0.00000001,
        number_of_epochs=1000, batch_size=1):
    """
    Performs stochastic gradient descient on the data entered using linear
    regression.
    """
    data = load_data(data_file_name)
    train_set_x, train_set_y = data[0]
    test_set_x, test_set_y = data[1]

    n_train= train_set_x.get_value(borrow=True).shape[0]

    index = T.lscalar('index')
    x = T.matrix('x')
    y = T.vector('y')

    regressor = LinearRegression(_input=x, n_in=3, n_out=1)

    cost = regressor.squared_error(y)

    g_theta = T.grad(cost = cost, wrt=regressor.theta)

    updates = {regressor.theta: regressor.theta - (learning_rate * g_theta) }

    train_model = theano.function(inputs=[index],
                                  outputs=cost,
                                  updates=updates,
                                  givens = {
                                      x:train_set_x[index:],
                                      y:train_set_y[index:]
                                      })#, mode='DEBUG_MODE')

    print('beginning training...')
    iter_count = 0
    old = 0
    new = float('inf')
    while (abs(old - new) >= 0.1):
        old = new
        print('iteration %d' % iter_count)
        new = train_model(0)
        print (regressor.theta.get_value())
        print(new)
        iter_count += 1

    print(regressor.theta.get_value())
    print(new)
    print('done')


def build_argument_parser():
    argument_parser = ArgumentParser()
    argument_parser.add_argument('--data-file-name', default='ex1data2.txt')
    return argument_parser

def main(argv=None):
    if argv is None:
        argv = sys.argv 
    argument_parser = build_argument_parser()
    args = argument_parser.parse_args(args=argv[1:])
    stochastic_gradient_descent(args.data_file_name)

if __name__ == '__main__':
    sys.exit(main())
