from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import logging
import os

import Image
import numpy
import theano

DEFAULT_DATA_FILE_NAME = os.path.join(os.path.dirname(__file__),
            '../../../data/eccv2010_beauty_data/eccv2010_split1.csv')

def load_images(hotornot_file_csv):
    """
    Assumes the images are in an immediate sub-directory if the csv file.
    """
    logging.info('loading data from %s' % hotornot_file_csv)
    hotornot_dir = os.path.join(os.path.dirname(__file__),
            '../../../data/eccv2010_beauty_data/hotornot_face')
    train_data = [[], []]
    test_data = [[], []]
    with open(hotornot_file_csv) as hotornot_csv:
        reader = csv.reader(hotornot_csv)
        def append_row_to_data(data, row):
            def get_array_from_image(image_name):
                image = Image.open(os.path.join(hotornot_dir, image_name))
                luma = image.convert('L')
                return numpy.asarray(luma).ravel()
            # append the x_data
            data[0].append(get_array_from_image(row[0]))
            data[1].append(row[1])
        for row in reader:
            if row[2] == 'train':
                append_row_to_data(train_data, row)
            elif row[2] == 'test':
                append_row_to_data(test_data, row)
            else:
                raise ValueError('only test or train allowed in input')
    
    train_data[0] = numpy.asarray(train_data[0], dtype=theano.config.floatX).T
    train_data[1] = numpy.asarray(train_data[1], dtype=theano.config.floatX).T
    test_data[0] = numpy.asarray(test_data[0], dtype=theano.config.floatX).T
    test_data[1] = numpy.asarray(test_data[1], dtype=theano.config.floatX).T
    logging.debug('train data shape: %s' % str(train_data[0].shape))
    logging.debug('test data shape: %s' %  str(test_data[0].shape))

    return train_data, test_data 

def to_theano_shared(data):
    data[0] = theano.shared(numpy.asarray(data[0], dtype=theano.config.floatX))
    data[1] = theano.shared(numpy.asarray(data[1], dtype=theano.config.floatX))
    return data


