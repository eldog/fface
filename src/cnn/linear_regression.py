#!/usr/bin/env python2.7

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import cPickle
import csv
import datetime
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

class TheanoLeastSquaresRegression(object):
    def __init__(self, x_data, n_features, m):
        self.theta = theano.shared(numpy.ones((n_features, 1),
                dtype=theano.config.floatX),
                name='theta')
        self.y_pred = T.dot(self.theta.T, x_data)
        self.m = m
    
    def cost(self, y):
        return (1 / (2 * self.m)) * T.sum(T.sqr(self.y_pred - y)) \
                + 0.01 * T.sum(T.sqr(self.theta))


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
    (x_train, y_train), (x_test, y_test), n, m, o = load_images(data_file_name)
    n_training_examples = m
    n_test_examples = o

    x = T.matrix('x')
    y = T.vector('y')

    l_r = theano.shared(learning_rate)

    tlsr = TheanoLeastSquaresRegression(x, n, n_training_examples)
    cost = tlsr.cost(y)
    test_model = theano.function([], outputs=cost,
                                 givens={x:x_test, y:y_test})
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
        print('cost %f' % current_cost)
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
        print(theta_tmp)
        print('cost: %f' % current_cost)
        iterations += 1

    return lsr.theta

def normalize_zero_mean(data):
    means = data.mean(axis=1)
    ranges = data.max(axis=1) - data.min(axis=1)
    return (numpy.subtract(data.T, means) / ranges).T

def plot(data_file_name, theta):
    (x_train, y_train), (x_test, y_test), n, m, o = load_images(data_file_name,
            theano_shared=False)
    #plot_data(x_train, y_train, theta)
    #plot_data(x_test, y_test, theta)
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
    y = map(float, y)
    print(x)
    print(y)
    pearsons = pearsonr(x[0],y) 
    print(pearsons)
    pyplot.title('Pearsons: %f' % pearsons[0])
    pyplot.show()

def load_images(hotornot_file_csv, theano_shared=True):
    """
    Assumes the images are in an immediate sub-directory if the csv file.
    """
    hotornot_dir = os.path.join(os.path.dirname(__file__),
            '../../../data/eccv2010_beauty_data/hotornot_face')

    train_data = [[], []]
    test_data = [[], []]
    with open(hotornot_file_csv) as hotornot_csv:
        reader = csv.reader(hotornot_csv)
        def append_row_to_data(data, row):
            def get_array_from_image(image_name):
                image = Image.open(os.path.join(hotornot_dir, image_name))
                luma = image.convert('L')
                return numpy.asarray(luma).ravel()
            # append the x_data
            data[0].append(get_array_from_image(row[0]))
            data[1].append(row[1])
        for row in reader:
            if row[2] == 'train':
                append_row_to_data(train_data, row)
            elif row[2] == 'test':
                append_row_to_data(test_data, row)
            else:
                raise ValueError('only test or train allowed in input')

    def to_theano_shared(data):
        data[0] = numpy.concatenate(
                    (numpy.ones((1, (data[0].shape[1]))), data[0]))
        data[1] = numpy.asarray(data[1])
        if theano_shared:
            data[0] = theano.shared(
                numpy.asarray(data[0], dtype=theano.config.floatX))
            data[1] = theano.shared(
                numpy.asarray(data[1], dtype=theano.config.floatX))

    train_data[0] = numpy.asarray(train_data[0], dtype=theano.config.floatX).T
    test_data[0] = numpy.asarray(test_data[0], dtype=theano.config.floatX).T

    #train_data[0] = normalize_zero_mean(train_data[0], means, ranges)
    #test_data[0] = normalize_zero_mean(test_data[0], means, ranges)

    mean = train_data[0].mean(axis=1)
    print(mean)
    #pyplot.imshow(mean.reshape(128,128), cmap=cm.Greys_r)
    #pyplot.show()
    A = (train_data[0].T - mean).T

    print('sigma time baby')
    x = T.matrix()
    
    covar = T.dot(x.T, x)

    f_covar = theano.function([x], covar) 

    sigma = f_covar(A)
    print('here we go')
    u, s, v = numpy.linalg.svd(sigma)
    print('done')
    face_space = numpy.dot(A, u)
    u_range = face_space[:,:100]
    print(u_range.shape)
    #pyplot.imshow(u_range.T[4].reshape(128,128), cmap=cm.Greys_r)

    #pyplot.show()
    #exit()
    train_data[0] = to_face_space(u_range, mean, train_data[0])
    test_data[0] = to_face_space(u_range, mean, test_data[0])
    n, m = train_data[0].shape
    n += 1 # we're going to add the ones on
    o = test_data[0].shape[1]
    to_theano_shared(train_data)
    to_theano_shared(test_data)

    return train_data, test_data, n, m, o
    
def to_face_space(face_space, mean_face, faces):
    """
    Projects a set of faces into face space
    """
    f_spaced_faces = []
    for face in faces.T:
        m_face = face - mean_face
        f_spaced_faces.append(numpy.dot(face_space.T, m_face))
    f_spaced_faces = numpy.asarray(f_spaced_faces).T
    print(f_spaced_faces.shape)

    return f_spaced_faces


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

default_file_name = os.path.join(os.path.dirname(__file__),
            '../../../data/eccv2010_beauty_data/eccv2010_split1.csv')

def build_argument_parser():
    argument_parser = ArgumentParser()
    argument_parser.add_argument('--data-file-name', default=default_file_name)
    argument_parser.add_argument('--reg-type', default='theano')
    argument_parser.add_argument('--learning-rate', type=float, default=0.13)
    return argument_parser

def main(argv=None):
    if argv is None:
        argv = sys.argv 
    argument_parser = build_argument_parser()
    args = argument_parser.parse_args(args=argv[1:])
    if args.reg_type == 'theano':
        print('theano')
        cost, theta, error = theano_sgd(args.data_file_name,
                learning_rate=args.learning_rate)
        print('cost %f' % cost)
        print('error %f' % error)
    else:
        print('normal')
        theta = sgd(args.data_file_name)
    print('THETA')
    print(theta)
    d_time = datetime.datetime.utcnow().strftime('%H:%M:%S-%d-%m-%Y')
    with open('out-%s.pickle' % d_time, 'w') as out_file:
        cPickle.dump(theta, out_file)
    plot(args.data_file_name, theta)

if __name__ == '__main__':
    sys.exit(main())
