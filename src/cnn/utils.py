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
           'append_timestamp_to_file_name', 'trim_to_batch_size', 'plot_cost',
           'normalize_zero_mean', 'get_means_and_ranges')

DEFAULT_DATA_FILE_NAME = os.path.join(os.path.dirname(__file__),
            '../../../data/eccv2010_beauty_data/eccv2010_split1.csv')

image_dir = os.path.join(os.path.dirname(__file__),
                         '../../../img/')
hotornot_dir = os.path.join(os.path.dirname(__file__),
            '../../../data/eccv2010_beauty_data/hotornot_face')
def load_images(hotornot_csv_file_name, convert_type='L'):
    """
    Loads the data from csv file and assumes the images are in an immediate 
    sub-directory if the csv file.

    :type str
    :param hotornot_csv_file_name: the name of the csv file which lists the data to
                                   be loaded
    """
    logging.info('loading data from %s' % hotornot_csv_file_name)
    train_data = [[], []]
    validation_data = [[], []]
    test_data = [[], []]
    test_data_file_names = []
    with open(hotornot_csv_file_name) as hotornot_csv:
        reader = csv.reader(hotornot_csv)
        def append_row_to_data(data, row):
            def get_array_from_image(image_name):
                image = Image.open(os.path.join(hotornot_dir, image_name))
                if convert_type == 'L':
                    image_data = image.convert(convert_type)
                elif convert_type ==  'YCvCr':
                    image_data = [numpy.asarray(i).ravel() for i in
                                  image.convert(convert_type).split()]
                else:
                    raise ValueError('Image convert type %s is not supported'
                                     % (convert_type))
                return numpy.asarray(image_data)
            # append the x_data

            y_cb_cr = get_array_from_image(row[0])
            data[0].append(y_cb_cr)
            data[1].append(row[1])
        for row in reader:
            if row[2] == 'train':
                append_row_to_data(train_data, row)
            elif row[2] == 'validation':
                append_row_to_data(validation_data, row)
            elif row[2] == 'test':
                append_row_to_data(test_data, row)
                test_data_file_names.append(row[0])
            else:
                raise ValueError('only test or train allowed in input')
   
    validation_data[0] = numpy.asarray(validation_data[0], dtype=theano.config.floatX)
    validation_data[1] = numpy.asarray(validation_data[1], dtype=theano.config.floatX)
    train_data[0] = numpy.asarray(train_data[0], dtype=theano.config.floatX)
    train_data[1] = numpy.asarray(train_data[1], dtype=theano.config.floatX)
    test_data[0] = numpy.asarray(test_data[0], dtype=theano.config.floatX)
    test_data[1] = numpy.asarray(test_data[1], dtype=theano.config.floatX)
    logging.debug('train data shape: %s' % str(train_data[0].shape))
    logging.debug('validation data shape is: %s' % str(validation_data[0].shape))
    logging.debug('test data shape: %s' % str(test_data[0].shape))

    return train_data, validation_data, test_data, test_data_file_names

def get_means_and_ranges(data):
    means = data.mean()
    ranges = data.max() - data.min()
    return means, ranges

def normalize_zero_mean(data, means, ranges):
    return (numpy.divide(numpy.subtract(data, means), ranges))

def trim_to_batch_size(data, batch_size):
    """
    Trims the data if need be to make sure it is indexable by the batch size
    
    :type two element list
    :param data: (x_data, y_data)

    :type int
    :param batch_size: the value the number examples in thedata's will be a 
                       multiple of
    """
    n_examples, n_channels, n_features = data[0].shape
    n_targets = data[1].shape[0]
    logging.debug('Have %d examples and %d targets' % (n_examples, n_targets))
    assert n_examples == n_targets
    remainder = n_examples % batch_size
    if remainder == 0:
        logging.info('Using %d examples in batches of %d'
                     % (n_examples, batch_size))
        return data
    logging.info('number of examples exceeds batch size by %d' % remainder)
    n_to_keep = n_examples - remainder
    data[0] = data[0][:n_to_keep]
    data[1] = data[1][:n_to_keep]
    logging.info('trimmed to %d examples' % n_to_keep)
    return data

def append_timestamp_to_file_name(file_name):
    d_time = datetime.datetime.utcnow().strftime('%H:%M:%S-%d-%m-%Y')
    return ('%s-%s' % (file_name, d_time))

def plot_correlation(human_scores, machine_scores, images, title, file_name, style='ro', 
                     show=False):
    pyplot.clf()
    #pyplot.plot(human_scores, machine_scores, style)
    import Image
    pyplot.axis([-4, 4, -4, 4])
    pyplot.xlabel('human score')
    pyplot.ylabel('machine score')
    pyplot.title(title, fontsize='small')
    pyplot.axes().set_aspect('equal', adjustable='box')
    for i, image in enumerate(images):
        pyplot.imshow(Image.open(os.path.join(hotornot_dir, image)),
            extent=(human_scores[i] + 0.2, human_scores[i] - 0.2,
                machine_scores[i] + 0.2, machine_scores[i] - 0.2))
        print(image, machine_scores[i])
    save_plot(file_name)
    if show:
        pyplot.show()

def save_plot(file_name):
    file_name = append_timestamp_to_file_name(file_name)
    figure_file_name = os.path.join(image_dir, '%s.png' % file_name)
    logging.info('writing plot of results to %s' % figure_file_name)
    with open(figure_file_name, 'wb') as figure_file:
        pyplot.savefig(figure_file, format='png')


def to_theano_shared(data):
    data[0] = theano.shared(numpy.asarray(data[0], dtype=theano.config.floatX),
            borrow=True)
    data[1] = theano.shared(numpy.asarray(data[1], dtype=theano.config.floatX),
            borrow=True)
    return data

def plot_cost(cost, validation, test, pearsons, title, file_name='cost', show=True):
    pyplot.clf()
    pyplot.autoscale(tight=True)
    pyplot.subplot(2, 1, 1)
    pyplot.plot(cost[0], cost[1], 'b', label='Training')
    pyplot.plot(validation[0], validation[1], 'g', label='Validation')
    pyplot.plot(test[0], test[1], 'c', label='Test')
    pyplot.title('Cost over iterations')
    pyplot.xlabel('Iterations')
    pyplot.ylabel('Cost')
    pyplot.ylim((0,50))
    pyplot.subplot(2, 1, 2)
    pyplot.plot(pearsons[0], pearsons[1], 'm')
    pyplot.xlabel('Iterations')
    pyplot.ylabel('Pearson product-moment correlation coefficient')
    pyplot.title('Pearson product-moment correlation coefficient over iterations')
    save_plot(file_name)
    if show:
        pyplot.show()

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
    logging.info('saving to %s' % pickle_file_name)
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
