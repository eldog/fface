#!/usr/bin/env python2.7
import numpy
import unittest

from plain_gradesc import load_data, sgd

class TestGradDesc(unittest.TestCase):
    def test_load_data_shape(self):
        x_data, y_data = load_data('ex1data2.txt')
        self.assertEqual(x_data.shape, (2,47))
        self.assertEqual(y_data.shape, (47,))

    def test_test_data(self):
        """ 
        We know what should be the minima for the handcrafted data
        """
        minima = sgd('test_data.csv')
        self.assertEqual(minima.all() ==  numpy.array([[2],[3]]).all())


if __name__ == '__main__':
    unittest.main()
