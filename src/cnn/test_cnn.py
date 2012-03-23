#!/usr/bin/env python2.7
from __future__ import print_function

import unittest

import cv
import cv2
import numpy
import theano
from theano import tensor as T

from convolution_neural_network import SingleLayerConvNN
from utils import *

class TestSingleLayerConvNN(unittest.TestCase):
    def setUp(self):
        self.rng = numpy.random.RandomState(2345)

    def test_output(self):
        x = T.tensor3('x')
        y = T.vector('y')
        batch_size = 1
        n_filters = 1
        image_shape = (batch_size, 1, 128, 128)
        # nodes, channels, filter width, filter height
        filter_shape = (n_filters, 1, 9, 9)
        pool_size = (8, 8)
        cnn = SingleLayerConvNN(self.rng,
                                x,
                                batch_size,
                                image_shape=image_shape,
                                filter_shape=filter_shape,
                                pool_size=pool_size)
        test_cnn = theano.function([x], cnn.regression.y_pred)
        test_conv = theano.function([x], cnn.layer_0.conv_out)
        # create a 1 x 1 x 8 x 8 array
        #test_image_data = numpy.array([[numpy.arange(64)]], 
        #                              dtype=theano.config.floatX)
        #test_image_data = numpy.array([[cv2.imread(
        #    '../../../data/eccv2010_beauty_data/hotornot_face/female_20_RRB8BYB_face_0.jpg',
        #    cv.CV_LOAD_IMAGE_GRAYSCALE).flatten()]], dtype=theano.config.floatX)

        test_image_data = numpy.array([[cv2.imread(
            '../../../data/eccv2010_beauty_data/hotornot_face/female_20_RRB8BYB_face_0.jpg',
            cv.CV_LOAD_IMAGE_GRAYSCALE).flatten()]], dtype=theano.config.floatX)


        #cnn.layer_0.W.set_value(numpy.ones(filter_shape,
        #                        dtype=theano.config.floatX))
        cnn.layer_0.b_c.set_value(numpy.asarray(self.rng.uniform(
                                                low=-0.006,
                                                high=0.006,
                                                size=(filter_shape[0],)),
                                                dtype=theano.config.floatX))
        cnn.layer_0.b.set_value(numpy.asarray(self.rng.uniform(
                                                low=-0.006,
                                                high=0.006,
                                                size=(filter_shape[0],)),
                                                dtype=theano.config.floatX))
        
        #self.assertEqual(cnn.regression.n_features, 9)
        theta_data = [0.1 for x in xrange(3*3*n_filters)]
        #cnn.regression.theta.set_value(numpy.array(theta_data,
        #                               dtype=theano.config.floatX).reshape(15*15*48,1))
        cnn.regression.bias.set_value(
                numpy.cast['float32'](self.rng.uniform(low=-0.6,
                                                       high=0.6,
                                                       size=(1,)))[0])

        cnn.regression.theta.set_value(numpy.asarray(self.rng.uniform(low=-0.006,
            high=0.006,
            size=(15*15*n_filters,1)), dtype=theano.config.floatX))

        mean, ranges = get_means_and_ranges(test_image_data)
        print('mean', mean)
        print('ranges', ranges)
        test_image_data = normalize_zero_mean(test_image_data, mean, ranges)
        print(test_image_data)
        conv_output = test_conv(test_image_data)
        print('conv out is %s' % conv_output[0][0])
        output = test_cnn(test_image_data)
        print('reg output is %f' % output)
        #self.assertEqual(output, (293.5)) 
        save_xml(cnn, 'test-rand-cnn.xml')

    def test_multi_parent(self):
        x = T.tensor3('x')
        y = T.vector('y')
        batch_size = 1
        n_filters = 2
        image_shape = (batch_size, 1, 4, 4)
        # nodes, channels, filter width, filter height
        filter_shape = (n_filters, 1, 3, 3)
        pool_size = (2, 2)
        cnn = SingleLayerConvNN(self.rng,
                                x,
                                batch_size,
                                image_shape=image_shape,
                                filter_shape=filter_shape,
                                pool_size=pool_size)
        test_conv = theano.function([x], cnn.layer_0.conv_out)
        test_sub = theano.function([x], cnn.layer_0.output)
        test_cnn = theano.function([x], cnn.regression.y_pred)

        # create a 1 x 1 x 2 x 2 array
        data = numpy.array([1, 1, 2, 2, 
                            1, 1, 2, 2, 
                            3, 3, 4, 4, 
                            3, 3, 4, 4]).reshape(4,4)
        test_image_data = numpy.array([data], 
                                       dtype=theano.config.floatX)

        cnn.layer_0.W.set_value(numpy.array([[[[1, 5, 8],
                                               [1, 2, 1],
                                               [7, 1, 1]]], 
                                             [[[2, 7, 5],
                                               [2, 3, 4],
                                               [6, 2, 2]]]],
                                            dtype=theano.config.floatX))
        #cnn.layer_0.W.set_value(numpy.ones(filter_shape,
        #                                    dtype=theano.config.floatX))
        cnn.layer_0.b_c.set_value(numpy.zeros((filter_shape[0],),
                                             dtype=theano.config.floatX))

        theta_data = [6.0, 7.0]# 8.0, 9.0, 11.0, 12.0, 13.0, 14.0]
        cnn.regression.bias.set_value(numpy.cast['float32'](2))

        cnn.regression.theta.set_value(
                numpy.asarray(
                       theta_data,
                       dtype=theano.config.floatX).reshape((2,1)))
        conv_output = test_conv(test_image_data)
        #print('conv out\n%s' % conv_output)
        sub_output = test_sub(test_image_data)
        #print('sub out \n%s' % sub_output)
        output = test_cnn(test_image_data)
        print('output is %f' % output)
        #self.assertEqual(output, (293.5)) 
        save_xml(cnn, 'test-cnn.xml')


if __name__ == '__main__':
    unittest.main()

