#!/usr/bin/env python2.7

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import sys

from argparse import ArgumentParser

from matplotlib import cm, pyplot
from mpl_toolkits.mplot3d import Axes3D
import numpy
from scipy.stats import pearsonr
import theano
from theano import tensor as T

class TheanoLeastSquaresRegression(object):
    def __init__(self, x_data, n_features, m):
        self.theta = theano.shared(numpy.ones((n_features, 1),
                dtype=theano.config.floatX),
                name='theta')
        self.y_pred = T.dot(self.theta.T, x_data)
        self.m = m
    
    def cost(self, y):
        return (1 / (2 * self.m)) * T.sum(T.sqr(self.y_pred - y)) + 0.01 * T.sum(T.sqr(self.theta))


class LeastSquaresRegression(object):
    def __init__(self, x_data, y_data):
        self.x = x_data
        self.y = y_data
        self.n, self.m = x_data.shape
        self.theta = numpy.ones((self.n, 1))
        
    def cost(self):
        return (1 / (2 * self.m )) \
                * ((numpy.dot(self.theta.T, self.x) - self.y) ** 2).sum()

    def derivative_cost_wrt_theta(self, theta_index):
        return (1 / self.m) \
                * ((numpy.dot(self.theta.T, self.x) - self.y) \
                        * self.theta[theta_index]).sum()

def theano_sgd(data_file_name, learning_rate=0.13):
    x_train, y_train, x_test, y_test = load_data(data_file_name)
    n_training_examples = x_train.shape[1]
    n_test_examples = x_test.shape[1]

    x_train = theano.shared(numpy.asarray(x_train, dtype=theano.config.floatX))
    y_train = theano.shared(numpy.asarray(y_train, dtype=theano.config.floatX))
    x_test = theano.shared(numpy.asarray(x_test, dtype=theano.config.floatX))
    y_test = theano.shared(numpy.asarray(y_test, dtype=theano.config.floatX))

    x = T.fmatrix('x')
    y = T.fvector('y')


    l_r = theano.shared(learning_rate)

    tlsr = TheanoLeastSquaresRegression(x, 3, n_training_examples)
    cost = tlsr.cost(y)
    test_model = theano.function([], outputs=cost,
                                 givens={x_data:x_test, y:y_test})
    g_theta = T.grad(cost,tlsr.theta)
    print(theano.pp(g_theta))
    updates = {tlsr.theta : tlsr.theta - l_r * g_theta}
    train_model = theano.function([], outputs=cost, updates=updates,
            givens={x:x_train, y:y_train})

    current_cost = train_model()
    print(current_cost)
    old_cost = 0
    iterations = 0
    while ((abs(current_cost- old_cost)) > 0.00001):
        if iterations > 300:
            l_r = learning_rate * 100
        print('iteration %d' % iterations)
        old_cost = current_cost
        current_cost = train_model()
        print(current_cost)
        print(tlsr.theta.get_value())
        iterations += 1

    validation = test_model()

    return current_cost, tlsr.theta.get_value(), validation


def sgd(data_file_name, learning_rate=0.0001):
    x_data, y_data, o, p = load_data(data_file_name)
    print('sgd', x_data)
    lsr = LeastSquaresRegression(x_data, y_data)
    current_cost = lsr.cost()
    print(current_cost)
    old_cost = 0
    iterations = 0 
    while ((abs(current_cost - old_cost)) > 0.00001):
        print('iteration %d' % iterations)
        theta_tmp = lsr.theta
        theta_tmp[0] =  (1 / lsr.m) * (numpy.dot(lsr.theta.T, lsr.x) - lsr.y).sum() 
        for j in xrange(1, lsr.theta.shape[0]):
            new_theta_value = theta_tmp[j] \
                           - learning_rate \
                           * lsr.derivative_cost_wrt_theta(j)
            theta_tmp[j] = new_theta_value
        old_theta = lsr.theta
        lsr.theta = theta_tmp
        old_cost = current_cost
        current_cost = lsr.cost()
        print(current_cost)
        print(theta_tmp)
        iterations += 1

    return lsr.theta

def normalize_zero_mean(data):
    means = data.mean(axis=1)
    ranges = data.max(axis=1) - data.min(axis=1)
    return (numpy.subtract(data.T, means) / ranges).T

def plot(data_file_name, theta):
    x_train, y_train, x_test, y_test = load_data(data_file_name)
    plot_data(x_train, y_train, theta)
    plot_data(x_test, y_test, theta)
    plot_correlation(x_test, theta, y_test)

def plot_data(x_data, y_data, theta):
    fig = pyplot.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x_data[1,:], x_data[2,:], y_data, linestyle="none", marker="o", mfc="none", markeredgecolor="red")
    ax.plot_wireframe(x_data[1,:], x_data[2,:], numpy.dot(theta.T, x_data).T)
    pyplot.show()
    x_data = normalize_zero_mean(x_data)

def plot_correlation(x_data, theta, y_data):
    x_guess = numpy.dot(theta.T, x_data).T
    pyplot.plot(x_guess, y_data, 'ro')
    pyplot.ylabel('real values')
    x = x_guess.T.tolist()
    y = y_data.tolist()
    print(x[0])
    print(y)
    pearsons = pearsonr(x[0],y) 
    print(pearsons)
    #plt.title('Pearsons: %f' % pearsons)
    pyplot.show()

def load_data(data_file_name):
    """
    Load the data assuming the label is the last on the row
    :type data_file_name: str
    :param data_file_name: the name of the file containing data
    """
    data = numpy.genfromtxt(data_file_name, dtype=int, delimiter=',')
    x_data = data[:, :-1].T
    x_data = normalize_zero_mean(x_data)
    # add the ones
    x_data = numpy.concatenate((numpy.ones((1, (x_data.shape[1]))), x_data))
    y_data  = data[:, -1]
    middle = len(y_data) / 2
    x_train = x_data[:, :middle]
    x_test = x_data[:, middle:]
    y_train = y_data[:middle]
    y_test = y_data[middle:]
    return x_train, y_train, x_test, y_test

def build_argument_parser():
    argument_parser = ArgumentParser()
    argument_parser.add_argument('--data-file-name', default='ex1data2.txt')
    argument_parser.add_argument('--reg-type', default='theano')
    return argument_parser

def main(argv=None):
    if argv is None:
        argv = sys.argv 
    argument_parser = build_argument_parser()
    args = argument_parser.parse_args(args=argv[1:])
    if args.reg_type == 'theano':
        print('theano')
        cost, theta, error = theano_sgd(args.data_file_name)
        print('cost %f', cost)
        print('error %f', error)
    else:
        print('normal')
        theta = sgd(args.data_file_name)
    print(theta)
    plot(args.data_file_name, theta)

if __name__ == '__main__':
    sys.exit(main())
