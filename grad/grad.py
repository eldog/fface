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

def load_data(data_file_name):
    """
    Load the data assuming the label is the last on the row
    :type data_file_name: str
    :param data_file_name: the name of the file containing data
    
    """
    data = numpy.genfromtxt(data_file_name, dtype=int, delimiter=',')
    features = data[:, :-1]
    labels = data[:, -1]
    return features, labels

def build_argument_parser():
    argument_parser = ArgumentParser()
    argument_parser.add_argument('--data-file-name', default='ex1data2.txt')
    return argument_parser

def main(argv=None):
    if argv is None:
        argv = sys.argv 
    argument_parser = build_argument_parser()
    args = argument_parser.parse_args(args=argv[1:])
    features, labels = load_data(args.data_file_name)

if __name__ == '__main__':
    sys.exit(main())
