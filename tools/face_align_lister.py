#!/usr/bin/env python3

import argparse
import csv
import os
import sys

def csv_to_list(csv_path, directory, out_file):
    directory = os.path.abspath(directory)
    count = 0 #hack
    with open(csv_path, 'r') as csv_file, open(out_file, 'w') as output_file:
        for row in csv.reader(csv_file):
            if count == 10:
                break
            output_file.write('%s\n' % os.path.join(directory, row[0]))
            count = count + 1
    
def get_argumnent_parser():
    parser = argparse.ArgumentParser(
            description='Create lists for facial alignment')
    parser.add_argument('faces_csv')
    parser.add_argument('faces_dir')
    parser.add_argument('out_dir')
    parser.add_argument('--faces_out', default='faces-out.txt')
    parser.add_argument('--align_out', default='align-out.txt')
    return parser 

def main(argv=None):
    if argv is None:
        argv = sys.argv
    parser= get_argumnent_parser()
    args = parser.parse_args(args=argv[1:])
    csv_to_list(args.faces_csv, args.faces_dir, args.faces_out)
    csv_to_list(args.faces_csv, args.out_dir, args.align_out)
    return 0
                                    
if __name__ == '__main__':
    exit(main())

