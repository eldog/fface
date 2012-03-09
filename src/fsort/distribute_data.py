#!/usr/bin/env python2.7
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from argparse import ArgumentParser
from collections import OrderedDict
import csv
import math
import os
import random
import sys

from matplotlib import pyplot
import Image
from numpy import exp
from scipy.stats import norm
from scipy import optimize


def calculate_sd(percentage_in_top, score_range):
    def cost(x):
        return abs(1 
                   - percentage_in_top 
                   - norm.cdf(score_range, loc=0, scale=x))
    return optimize.fmin(cost, 2)[0]

def get_percentage_in_range(start, end, sd):
    return norm.cdf(end, loc=0, scale=sd) - norm.cdf(start, loc=0, scale=sd)

def get_normalised_scores(ranked_data, percentage_in_top=0.02, score_range=5):
    sd = calculate_sd(percentage_in_top, score_range)
    scores = []
    n_data = len(ranked_data)
    bucket_start = 0

    # bottom run 
    bucket_end = n_data * norm.cdf(-score_range, loc=0, scale=sd)
    bucket_end = int(math.floor(bucket_end))
    bucket_size = len(ranked_data[:bucket_end])
    for j in range(bucket_size):
        scores.append(-score_range)
    bucket_start += bucket_end

    # main bell
    for i in range(-score_range, score_range + 1):
        bucket_end = n_data * get_percentage_in_range(i, i+1, sd)
        bucket_end = int(math.ceil(bucket_end))
        bucket = ranked_data[bucket_start:bucket_start+bucket_end]
        bucket_size = len(bucket)
        for j in xrange(bucket_size):
            scores.append(i + j / bucket_size)
        bucket_start += bucket_end

    # top run
    #bucket_end = n_data * norm.sf(score_range, loc=0, scale=sd)
    #bucket_end = int(math.floor(bucket_end))
    bucket_size = len(ranked_data[bucket_start:])
    for j in range(bucket_size):
        scores.append(score_range + 1)

    return scores

def remove_bad_faces(clean_file_path, data):
    with open(clean_file_path) as clean_file:
        clean_data = set()
        for row in csv.reader(clean_file):
            clean_data.add(row[0])
    cleaned_data = []
    for datum in data:
        if datum in clean_data:
            cleaned_data.append(datum)
    return cleaned_data
    

def gaussian(height, center_x, center_y, width_x, width_y):
    """Returns a gaussian function with the given parameters"""
    return lambda x,y: height*exp(
                    -(((center_x-x)/width_x)**2+((center_y-y)/width_y)**2)/2)

def sigmoid(height, width):
    return lambda x: height / (width + exp(-x))

def get_data_from_file(rank_file_path):
    with open(rank_file_path) as rank_file:
        data = []
        for datum in rank_file:
            datum = datum.strip()
            if datum:
                data.append(datum)
    return data

def plot_distibution(data, distribution_scores):
    pyplot.plot(xrange(len(data)), distribution_scores)
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
    argument_parser.add_argument('clean_data_file_path',
                                help='the path to the clean data')
    argument_parser.add_argument('out_csv_file_path',
                                 help='The csv file to write out the data to')
    return argument_parser

def main(argv=None):
    if argv is None:
        argv = sys.argv
    argument_parser = build_argument_parser()
    args = argument_parser.parse_args(argv[1:])
    
    data = get_data_from_file(args.rank_file_path)
    data = remove_bad_faces(args.clean_data_file_path, data)
    distributed_scores = get_normalised_scores(data, percentage_in_top=0.001,
                                               score_range=5)
    assert(len(data) == len(distributed_scores))
    plot_distibution(data, distributed_scores)
    data_scores = zip(data, distributed_scores)
    randomized_data = randomize_data(data_scores)
    labelled_data = label_data(randomized_data)
    write_csv(labelled_data, args.out_csv_file_path)


if __name__ == '__main__':
    exit(main())


