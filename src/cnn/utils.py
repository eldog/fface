from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import csv
import datetime
import logging
import os
import pickle

import Image
from matplotlib import pyplot
import numpy
import theano

__all__ = ('DEFAULT_DATA_FILE_NAME', 'get_face_space', 'load_images',
           'plot_correlation', 'save_pickle', 'get_pickle', 'to_theano_shared',
           'append_timestamp_to_file_name')

DEFAULT_DATA_FILE_NAME = os.path.join(os.path.dirname(__file__),
            '../../../data/eccv2010_beauty_data/eccv2010_split1.csv')

image_dir = os.path.join(os.path.dirname(__file__),
                         '../../../img/')

def load_images(hotornot_csv_file_name):
    """
    Loads the data from csv file and assumes the images are in an immediate 
    sub-directory if the csv file.

    :type str
    :param hotornot_csv_file_name: the name of the csv file which lists the data to
                                   be loaded
    """
    logging.info('loading data from %s' % hotornot_csv_file_name)
    hotornot_dir = os.path.join(os.path.dirname(__file__),
            '../../../data/eccv2010_beauty_data/hotornot_face')
    train_data = [[], []]
    test_data = [[], []]
    with open(hotornot_csv_file_name) as hotornot_csv:
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
    logging.debug('test data shape: %s' % str(test_data[0].shape))

    return train_data, test_data 

def append_timestamp_to_file_name(file_name):
    d_time = datetime.datetime.utcnow().strftime('%H:%M:%S-%d-%m-%Y')
    return ('%s-%s' % (file_name, d_time))

def plot_correlation(human_scores, machine_scores, title, file_name, style='ro', 
                     show=False):
    pyplot.plot(human_scores, machine_scores, style)
    pyplot.axis([-4, 4, -4, 4])
    pyplot.xlabel('human score')
    pyplot.ylabel('machine score')
    pyplot.title(title, fontsize='small')
    if show:
        pyplot.show()
    file_name = append_timestamp_to_file_name(file_name)
    figure_file_name = os.path.join(image_dir, '%s.png' % file_name)
    logging.info('writing scatterplot of results to %s' % figure_file_name)
    with open(figure_file_name, 'w') as figure_file:
        pyplot.savefig(figure_file, format='png')

def to_theano_shared(data):
    data[0] = theano.shared(numpy.asarray(data[0], dtype=theano.config.floatX))
    data[1] = theano.shared(numpy.asarray(data[1], dtype=theano.config.floatX))
    return data

pickle_dir = os.path.join(os.path.dirname(__file__), '../../../data/pickles')

def get_face_space(file_name, data_type, data, eigface):
    pickle_name = '%s-%d-%s' % (os.path.basename(file_name), eigface.n_eigs, data_type)
    pickle = get_pickle(pickle_name)
    if pickle is not None:
        logging.info('loading previously calculated data for %s' % data_type)
        return pickle
    else:
        face_space = eigface.project_to_face_space(data)
        save_pickle(face_space, pickle_name)
        return face_space

def _create_pickle_file_name(file_name):
    return '%s.pkl' % os.path.join(pickle_dir, file_name)

def save_pickle(obj, file_name):
    """
    Pickles an object and writes it to the pickle directory

    :type object
    :param obj: the object to be pickled

    :type str
    :param file_name: the name of the pickle file to be written to
    """
    pickle_file_name = _create_pickle_file_name(os.path.basename(file_name))
    with open(pickle_file_name, 'wb') as pickle_file:
        pickle.dump(obj, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)

def get_pickle(pickle_name):
    """
    Returns the pickled object if it exists otherwise returns None
    
    :type str
    :param pickle_name: the name of the pickle file to be loaded
    """
    pickle_file_name = _create_pickle_file_name(os.path.basename(pickle_name))
    if os.path.basename(pickle_file_name) in os.listdir(pickle_dir):
        with open(pickle_file_name, 'rb') as pickle_file:
            return pickle.load(pickle_file)
    return None
