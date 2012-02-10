#!/usr/bin/env python2.7
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import logging
import sys

from matplotlib import pyplot
import numpy
from scipy.stats import pearsonr

from eigenface import EigenFace
from utils import DEFAULT_DATA_FILE_NAME, load_images

def plot_correlation(real_scores, predictions):
    pyplot.plot(real_scores, predictions, 'ro')
    pyplot.axis([-4, 4, -4, 4])
    pyplot.xlabel('human scores')
    pyplot.ylabel('machine scores')
    pearsons = pearsonr(real_scores, predictions)
    logging.info('pearsons correlation: %f, %f' % pearsons)
    pyplot.title('Scatter of scores with pearsons correlation %f'% pearsons[0], 
                 fontsize='small')
    pyplot.show() 

def knn_regression(data_file_name, k_value=3, n_eigs=100):
    train_data, test_data = load_images(data_file_name)
    eig_face = EigenFace(train_data[0], n_eigs=n_eigs)
    train_data[0] = eig_face.project_to_face_space(train_data[0])
    test_data[0] = eig_face.project_to_face_space(test_data[0])
    logging.info("Beginning knn regression")
    predictions = []
    errors = []
    n_test_examples = test_data[0].shape[1]
    real_scores = test_data[1].T.tolist()
    train_data = zip(train_data[0].T, train_data[1])
    test_data = zip(test_data[0].T, test_data[1])
    for iterations, (test_example, test_score) in enumerate(test_data):
        logging.info('on example %d of %d' % (iterations, n_test_examples))
        distances = []
        for train_example, train_score in train_data:
            distance = (numpy.sqrt(
                                numpy.sum(
                                    numpy.square(
                                        test_example - train_example))))
            distances.append((distance, train_score))
        distances.sort()
        k_nearest_neighbours = distances[:k_value]
        prediction = sum(score for distance, score in k_nearest_neighbours)\
                     / k_value
        predictions.append(prediction)
        error = abs(test_score - prediction)
        logging.info('error is %f' % error)
        errors.append(error)
    logging.info('mean error is %f' % (sum(errors) / len(errors)))
    plot_correlation(real_scores, predictions)

def build_argument_parser():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument('--data-file-name', nargs='+',
                                 default=[DEFAULT_DATA_FILE_NAME])
    argument_parser.add_argument('--k-value', type=int, default=3)
    argument_parser.add_argument('--n-eigs', type=int, default=100)
    argument_parser.add_argument('--log-level', default='INFO')
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
    for data_file in args.data_file_name:
        knn_regression(data_file, k_value=args.k_value, n_eigs=args.n_eigs)

if __name__ == '__main__':
    exit(main())
