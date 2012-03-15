#!/usr/bin/env python2.7

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from argparse import ArgumentParser
import math
import os
import sys

import Image
import numpy

class CArray(object):
    """
    Represents an array definition in C

    """
    ASCENDING = 'ascending'
    ONES = 'ones'
    OPTIONS = [ASCENDING, ONES]

    def __init__(self, n_items_in_array, width, array_type):
        """
        :type n_items_in_array: int
        :param n_items_in_array:  the number of items to be represented in array

        :type width: int

        :param width: the number of elements that will be printed per line

        """
        assert n_items_in_array > 0
        assert array_type in self.OPTIONS
        self.array_type = array_type
        self.set_array(n_items_in_array)
        self.width = width

    def set_array(self, n_items_in_array):
        if self.array_type == self.ASCENDING:
            self.array = range(n_items_in_array)
        elif self.array_type == self.ONES:
            self.array = [1 for x in xrange(n_items_in_array)]
        else:
            raise ValueError('array type is unknown')

    def __str__(self):
        padding = int(math.ceil(math.log10(len(self.array))) + 1)
        fmt_str = '%%%dd' % (padding,)
        str_list = ['{\n']
        for index, item in enumerate(self.array):
            mod = index % self.width
            if mod == 0:
                str_list.append('    ')
            
            if index == len(self.array) - 1:
                seperator = '\n'
            elif mod == self.width - 1:
                seperator = ',\n'
            else:
                seperator = ', '
            
            str_list.extend([fmt_str % (item,), seperator])
        str_list.append('}\n')
        return ''.join(str_list)

    def to_file(self, file_path, image=False):
        with open(file_path, 'w') as output_file:
            output_file.write(str(self))
        if image:
            height = int(len(self.array) / self.width)
            rgb_data = [[val, val, val] for val in self.array]
            data = numpy.array(rgb_data, dtype=numpy.uint8).reshape(self.width,
                                                                    height,
                                                                    3)
            output_image = Image.fromarray(data)
            with open('%s.bmp' % os.path.splitext(file_path)[0], 'w') as image_output_file:
                output_image.save(image_output_file)


def build_argument_parser():
    argument_parser = ArgumentParser()
    argument_parser.add_argument('n_items_in_array',
                                 type=int)
    argument_parser.add_argument('array_width',
                                 type=int)
    argument_parser.add_argument('output_file_path')
    argument_parser.add_argument('array_type',
                                 type=str,
                                 choices=CArray.OPTIONS)
    argument_parser.add_argument('--image',
                                 action='store_true')
    return argument_parser

def main(argv=None):
    if argv is None:
        argv = sys.argv
    argument_parser = build_argument_parser()
    args = argument_parser.parse_args(args=argv[1:])
    c_array = CArray(args.n_items_in_array, 
                     args.array_width,
                     args.array_type)
    c_array.to_file(args.output_file_path, image=args.image)

if __name__ == '__main__':
    exit(main())

