from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy
import theano
from theano import tensor as T

class TheanoLeastSquaresRegression(object):
    """Calculates the least-squares error of input data to target data"""
    def __init__(self, x_data, n_features, m, reg_lambda=0.1, theta=None, bias=None):
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
        if theta is None:
            theta = theano.shared(numpy.zeros((n_features, 1),
                dtype=theano.config.floatX),
                name='theta')
        self.theta = theta
        if bias is None:
            bias = theano.shared(numpy.cast['float32'](0),
                    name='bias')
        self.bias = bias
        self.y_pred = T.dot(self.theta.T, x_data) + self.bias
        self.m = m
        self.reg_lambda = reg_lambda
        self.params = [self.theta, self.bias]


    def cost(self, y):
        """
        Returns the cost of the current prediction function.
        """
        return (1 / (2 * self.m)) * T.sum(T.sqr(self.y_pred - y)) \
                + self.reg_lambda * T.sum(T.sqr(self.theta))

    def error(self, y):
        return (numpy.divide(numpy.subtract(y, self.y_pred), y))

    def __getstate__(self):
        return (self.theta, self.b, self.reg_lambda)


