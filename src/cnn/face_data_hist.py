#!/usr/bin/env python

from argparse import ArgumentParser
import csv
import os
import sys

from matplotlib import pyplot

from linear_regression import default_file_name

def plot_histogram(scores_data):
    pyplot.hist(scores_data)
    pyplot.show()

def load_score_data(data_file_name):
    with open(data_file_name, 'r') as data:
        reader = csv.reader(data)
        scores = []
        for row in reader:
            scores.append(float(row[1]))
    return scores

def build_argumentparser():
    argument_parser = ArgumentParser()
    argument_parser.add_argument('--data-file-name', default=default_file_name)
    return argument_parser

def main(argv=None):
    if argv is None:
        argv = sys.argv
    argument_parser = build_argumentparser()
    args = argument_parser.parse_args(args=argv[1:])
    score_data = load_score_data(args.data_file_name)
    plot_histogram(score_data)

if __name__ == '__main__':
    exit(main())
