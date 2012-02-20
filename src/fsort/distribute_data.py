#!/usr/bin/env python2.7
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from argparse import ArgumentParser
import csv
import os
import random
import sys

from matplotlib import pyplot
import Image
from numpy import exp

def gaussian(height, center_x, center_y, width_x, width_y):
    """Returns a gaussian function with the given parameters"""
    return lambda x,y: height*exp(
                    -(((center_x-x)/width_x)**2+((center_y-y)/width_y)**2)/2)

def sigmoid(height, width):
    return lambda x: height / (width + exp(-x))

def get_data_from_file(rank_file_path):
    with open(rank_file_path, 'r') as rank_file:
        data = rank_file.read().split('\n')
    return data

def get_ranks_from_data(data):
    ranks = range(-len(data) // 2, len(data) // 2)
    ranked_data = zip(data, ranks)
    return ranked_data

def plot_distibution(ranks, distribution_scores):
    pyplot.plot([x for u, x in ranks], distribution_scores)
    pyplot.show()

def write_csv(scored_data, csv_file_path):
    with open(csv_file_path, 'w') as csv_file:
        writer = csv.writer(csv_file)
        for (face_file, score), label in scored_data:
            writer.writerow([face_file, score, label])

def randomize_data(data):
    random.seed(1234)
    random.shuffle(data)
    return data

def label_data(data):
    n_train = len(data) // 2
    n_validation = n_train // 3
    n_test = len(data) - n_train - n_validation
    labels = []
    for i in xrange(n_train):
        labels.append('train')
    for i in xrange(n_validation):
        labels.append('validation')
    for i in xrange(n_test):
        labels.append('test')
    return zip(data, labels)

def build_argument_parser():
    argument_parser = ArgumentParser()
    argument_parser.add_argument('rank_file_path',
                                 help='the path to the file containing the'
                                 'ordered image names')
    argument_parser.add_argument('out_csv_file_path',
                                 help='The csv file to write out the data to')
    return argument_parser

def main(argv=None):
    if argv is None:
        argv = sys.argv
    argument_parser = build_argument_parser()
    args = argument_parser.parse_args(argv[1:])
    data = get_data_from_file(args.rank_file_path)
    ranks = get_ranks_from_data(data)
    gaussians = gaussian(10, 1024, 0, 750, 300)
    sigmoids = sigmoid(1, 1)
    distributed_scores = [gaussians(x, 100) for u, x in ranks]
    plot_distibution(ranks, distributed_scores)
    randomized_data = randomize_data(zip(data, distributed_scores))
    labelled_data = label_data(randomized_data)
    write_csv(labelled_data, args.out_csv_file_path)


if __name__ == '__main__':
    exit(main())


