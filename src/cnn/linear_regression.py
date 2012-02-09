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
    """Calculates the least-squares error of input data to target data"""
    def __init__(self, x_data, n_features, m, reg_lambda=0.1):
        """
        Create the weights and prediction function.
        
        :type x_data: numpy.ndarray
        :parameter x_data: the input data to be used for the prediction
                           function.

        :type n_features: int
        :parameter n_features: the number of features of x_data.

        :type m: int
        :parameter m: the number of examples in x_data
        """
        self.theta = theano.shared(numpy.zeros((n_features, 1),
                dtype=theano.config.floatX),
                name='theta')
        self.bias = theano.shared(0.0,
                    name='bias')
                        
        self.y_pred = T.dot(self.theta.T, x_data) + self.bias
        self.m = m
        self.reg_lambda = reg_lambda
    
    def cost(self, y):
        """
        Returns the cost of the current prediction function.
        """
        return (1 / (2 * self.m)) * T.sum(T.sqr(self.y_pred - y)) \
                + self.reg_lambda * T.sum(T.sqr(self.theta))


class EigenFace(object):
    """Calculated the eigenfaces of a given set of faces"""

    def __init__(self, faces, n_eigs=100):
        """
        Create the facespace of a given set of faces.

        :type faces: numpy.ndarray
        :param faces: an n x m dimensional array of face image data

        :type n_eigs: int
        :param n_eigs: the number of dimensions that the facespace should
                       have. It will be a n_eigs x m dimensional array.
        """
        # convert face data to correct type for theano to use gpu
        faces = numpy.asarray(faces, dtype=theano.config.floatX)
        
        # calculate the mean face, Psi
        self.mean_face = faces.mean(axis=1)
        # create the face space, i.e., the eigenvectors of the faces
        face_diffs = (faces.T - self.mean_face).T
        x = T.matrix()
        covar = T.dot(x.T, x)
        f_covar = theano.function([x], covar) 
        sigma = f_covar(face_diffs)
        u, s, v = numpy.linalg.svd(sigma)
        # take the first n_eigs eigenfaces for facespace
        self.face_space = numpy.dot(face_diffs, u)[:,:n_eigs]

    def project_to_face_space(self, faces):
        """
        Returns a set of faces projected into the face space

        :type faces: numpy.ndarray
        :param faces: an n x p dimensional array of face image data
        """
        f_spaced_faces = []
        for face in faces.T:
            face_diff = face - self.mean_face
            f_spaced_faces.append(numpy.dot(self.face_space.T, face_diff))
        return numpy.asarray(f_spaced_faces).T


def plot_correlation(x_data, theta, bias, y_data):
    print(x_data.shape)
    print(theta.shape)
    x_guess = (numpy.dot(theta.T, x_data) + bias).T
    pyplot.plot(x_guess, y_data, 'ro')
    pyplot.axis([-4, 4, -4, 4])
    pyplot.ylabel('real values')
    x = x_guess.T.tolist()
    y = y_data.tolist()
    y = map(float, y)
    pearsons = pearsonr(x[0],y) 
    print('pearsons coefficient: %f' % pearsons[0])
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
    
    
    train_data[0] = numpy.asarray(train_data[0], dtype=theano.config.floatX).T
    train_data[1] = numpy.asarray(train_data[1], dtype=theano.config.floatX).T
    test_data[0] = numpy.asarray(test_data[0], dtype=theano.config.floatX).T
    test_data[1] = numpy.asarray(test_data[1], dtype=theano.config.floatX).T
    return train_data, test_data 

def to_theano_shared(data):
    
    data[0] = theano.shared(numpy.asarray(data[0], dtype=theano.config.floatX))
    data[1] = theano.shared(numpy.asarray(data[1], dtype=theano.config.floatX))
    return data

default_file_name = os.path.join(os.path.dirname(__file__),
            '../../../data/eccv2010_beauty_data/eccv2010_split1.csv')

def prepend_ones(data):
    return numpy.concatenate((numpy.ones((1, (data.shape[1])), 
                                dtype=theano.config.floatX), data))


def eigface_sgd(data_file_name, learning_rate=0.000000000000000001, 
                reg_lambda=0.1):
    train_data, test_data = load_images(data_file_name)
    eig_face = EigenFace(train_data[0])
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
    print(x_test)
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
    print(current_cost)
    old_cost = 0
    iterations = 0
    while ((abs(current_cost- old_cost)) > 0.000001):
        old_cost = current_cost
        current_cost = train_model()
        if iterations % 1000 == 0:
            print('iteration %d' % iterations)
            print('cost %f' % current_cost)
        iterations += 1

    error = test_model()
    theta = tlsr.theta.get_value()
    bias = tlsr.theta.get_value()

    # Print the results
    print('training cost minimised:\t\t %f' % current_cost)
    print('test error:\t\t\t %f' % error)

    # Save our weights should we ever need them again
    d_time = datetime.datetime.utcnow().strftime('%H:%M:%S-%d-%m-%Y')
    theta_file_name = 'out-%s.pickle' % d_time
    print('writing weights to %s' % theta_file_name)
    with open(theta_file_name, 'w') as out_file:
        cPickle.dump((theta, bias), out_file)

    plot_correlation(x_test.get_value(), theta, bias, y_test.get_value())

def build_argument_parser():
    argument_parser = ArgumentParser()
    argument_parser.add_argument('--data-file-name', default=default_file_name)
    argument_parser.add_argument('--learning-rate', type=float,
            default=0.000000000000000001)
    argument_parser.add_argument('--reg-lambda', type=float, default=0.1)
    return argument_parser

def main(argv=None):
    if argv is None:
        argv = sys.argv 
    argument_parser = build_argument_parser()
    args = argument_parser.parse_args(args=argv[1:])
    eigface_sgd(args.data_file_name, learning_rate=args.learning_rate,
            reg_lambda=args.reg_lambda)
    
if __name__ == '__main__':
    sys.exit(main())
