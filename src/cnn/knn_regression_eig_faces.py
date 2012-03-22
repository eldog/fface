#!/usr/bin/env python2.7
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import logging
import sys
from math import exp
import os

import numpy
from scipy.stats import pearsonr

from eigenface import EigenFace
from utils import * 

def knn_regression(data_file_name, k_value=3, n_eigs=100, weighted=True, 
                   beta=1000000):
    train_data, test_data, file_names = old_load_images(data_file_name)
    eig_face = EigenFace.from_file(train_data[0], data_file_name, n_eigs)
    train_data[0] = get_face_space(data_file_name, 'train_x', train_data[0],
                                   eig_face)
    test_data[0] = get_face_space(data_file_name, 'test_x', test_data[0],
                                  eig_face)
    logging.info("Beginning knn regression")
    predictions = []
    errors = []
    n_test_examples = test_data[0].shape[1]
    real_scores = test_data[1].T.tolist()
    train_data = zip(train_data[0].T, train_data[1])
    test_data = zip(test_data[0].T, test_data[1])
    for iterations, (test_example, test_score) in enumerate(test_data):
        if iterations % 100 == 0:
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
        if weighted:
            sum_weighted_distances = sum(score * exp(-distance / beta) 
                                     for distance, score in 
                                     k_nearest_neighbours)
            normalisation = sum(exp(-distance / beta) for distance, score in 
                                k_nearest_neighbours)
            prediction = (1 / normalisation) * sum_weighted_distances
        else:
            prediction = sum(score for distance, score in k_nearest_neighbours)\
                         / k_value
        predictions.append(prediction)
        error = abs(test_score - prediction)
        errors.append(error)
    logging.info('mean error is %f' % (sum(errors) / len(errors)))
    return real_scores, predictions, file_names

def build_argument_parser():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument('--data-file-name', nargs='+',
                                 default=[DEFAULT_DATA_FILE_NAME])
    argument_parser.add_argument('--k-value', type=int, default=3)
    argument_parser.add_argument('--beta', type=float, default=1000000)
    argument_parser.add_argument('--n-eigs', type=int, default=100)
    argument_parser.add_argument('--show-plot', action='store_true')
    argument_parser.add_argument('--not-weighted', action='store_false')
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
        real_scores, predictions, file_names = knn_regression(data_file, 
                                        k_value=args.k_value, 
                                        n_eigs=args.n_eigs,
                                        beta=args.beta,
                                        weighted=args.not_weighted)
        pearsons = pearsonr(real_scores, predictions)
        logging.info('pearsons correlation: %f, %f' % pearsons)
        title = 'KNN on data set %s with k=%d beta=%d ' \
                'neigfaces=%d pearsons:%f' % (os.path.basename(data_file), 
                                              args.k_value, args.beta, 
                                              args.n_eigs, pearsons[0])
        file_name = 'KNN-k%d-b%d-e%d' % (args.k_value, args.beta, args.n_eigs)
        plot_correlation(real_scores, predictions, file_names, title, file_name, style='bo',
                         show=args.show_plot, pearsons=pearsons)

if __name__ == '__main__':
    exit(main())
