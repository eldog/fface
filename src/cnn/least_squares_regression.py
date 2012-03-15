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
        self.n_features = n_features
        self.m = m
        self.reg_lambda = reg_lambda
        self.params = [self.theta, self.bias]


    def cost(self, y):
        """
        Returns the cost of the current prediction function.
        """
        return T.sum(T.sqr(self.y_pred - y))

    def error(self, y):
        return (numpy.divide(numpy.subtract(y, self.y_pred), y))

    def to_xml(self, document, parent):
        plane = document.createElement('plane')
        plane.setAttribute('id', 'output')
        plane.setAttribute('type', 'regression')
        plane.setAttribute('neuronsize', '15x15')
        parent.appendChild(plane)

        bias = document.createElement('bias')
        plane.appendChild(bias)
        bias_text = document.createTextNode(str(self.bias.get_value()))
        bias.appendChild(bias_text)
        index = 0

        # splits array into evenly sized chunks
        def chunk(l, step):
            return [l[i:i+step] for i in xrange(0, len(l), step)]

        chunks = chunk(self.theta.get_value().flatten().tolist(), 15 * 15)
        for i, value  in enumerate(chunks):
            connection = document.createElement('connection')
            connection.setAttribute('to', 'sub%d' % (i,))
            plane.appendChild(connection)
            weights_text = ''.join([x.strip(',') for x in
                str(chunks).strip('[]')])
            connection_text = document.createTextNode(weights_text)
            connection.appendChild(connection_text)

    def __getstate__(self):
        return (self.theta, self.b, self.reg_lambda)


