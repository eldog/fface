#!/usr/bin/env python2.7
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from argparse import ArgumentParser
import os
import shutil
import sys

def build_argument_parser():
    argument_parser = ArgumentParser()
    argument_parser.add_argument('ranked_file_path',
                                 help='The file listing ordered data')
    argument_parser.add_argument('image_dir',
                                 help='The directory of the images')
    argument_parser.add_argument('out_path',
                                 help='the directory to copy the files to')
    return argument_parser

def move_data(move_pairs, image_dir, out_path):
    if not os.path.isdir(out_path):
        os.mkdir(out_path)
    for (cur, new) in move_pairs:
        print('copying %s to %s' % (cur, out_path))
        shutil.copy(os.path.join(image_dir, cur),
                    os.path.join(out_path, new))

def rename_data(data):
    return ['%d.jpg' % i for i, datum in enumerate(data)]

def read_data(ranked_file_path):
    with open(ranked_file_path) as ranked_file:
        data = []
        for datum in ranked_file:
            datum = datum.strip()
            if datum:
                data.append(datum)
    return data

def main(argv=None):
    if argv is None:
        argv = sys.argv
    argument_parser = build_argument_parser()
    args = argument_parser.parse_args()
    data = read_data(args.ranked_file_path)
    renamed_data = rename_data(data)
    move_data(zip(data,renamed_data), args.image_dir, args.out_path)

if __name__ == '__main__':
    exit(main())
