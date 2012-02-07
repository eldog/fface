#!/usr/bin/env python2.7
from __future__ import division

import argparse
import csv
import logging
import os
import math
import pprint
import numpy
from threading import Lock
from PIL import Image
from foxxy.threading.pool import ThreadPool

class EigFace(object):
    def __init__(self, number_of_eig_faces=10, 
                 log_level=logging.INFO):
        self._number_of_eig_faces = number_of_eig_faces
        self.logger = logging.getLogger('eigface')
        self.logger.setLevel(log_level)

    def create_eig_faces(self, data):
        self._create_average_face_and_load_face_data(data)    
        self._save_average_face_image()  
        self._find_eig_faces()
        self._save_eig_face_images()
 
    def _create_average_face_and_load_face_data(self, data):
        sum_of_faces_so_far = None
        self._faces = []
        self._image_size = None
        for face_file in data:
            self.logger.info('processing image %s' % face_file)
            face_img = Image.open(face_file)
            if self._image_size is None:
                self._image_size = face_img.size
                print self._image_size
            elif face_img.size != self._image_size:
                raise ValueError('Images not all the same size! Oh dear.')
            # Turn into an array int32 to prevent rollover and
            # unravel the 2d face data into a 1d array
            face_data = numpy.array(face_img, dtype='float_')
            face_data = face_data.ravel()
            self._faces.append(face_data)
            if sum_of_faces_so_far is None:
                sum_of_faces_so_far = face_data
            else:
                sum_of_faces_so_far = sum_of_faces_so_far + face_data
        # Take the mean of the face data in a format for JPEG images
        self._average_face_data = numpy.array(
                sum_of_faces_so_far // len(self._faces))
        self._average_face_data = self._average_face_data.ravel()

    def _save_average_face_image(self):
        self._save_vector(self._average_face_data, 'average-face.jpg')

    def _find_eig_faces(self):
        self._diffs_of_faces_from_average = []
        for face in self._faces:
            self._diffs_of_faces_from_average.append(
                    face - self._average_face_data)
        number_of_faces = len(self._diffs_of_faces_from_average)
        self._diffs_of_faces_from_average = numpy.array(self._diffs_of_faces_from_average)
        faces_dot_products = numpy.dot(
                        self._diffs_of_faces_from_average,
                        self._diffs_of_faces_from_average.T)
        self.logger.info('calculating eig vectors')
        eig_values, eig_vectors = numpy.linalg.eig(faces_dot_products)
        eig_value_vector_pairs = zip(eig_values, eig_vectors)
        eig_value_vector_pairs.sort()
        #eig_value_vector_pairs.reverse()
        del eig_value_vector_pairs[self._number_of_eig_faces:]
        sorted_eig_vectors = map(lambda x : x[1], eig_value_vector_pairs)
        self._diffs_of_faces_from_average = numpy.matrix(
                self._diffs_of_faces_from_average)
        self._eig_faces = []
        for i, eig_vector in enumerate(sorted_eig_vectors):
            eig_vector = numpy.matrix(eig_vector)
            eig_face = eig_vector * self._diffs_of_faces_from_average
            self._eig_faces.append(eig_face.ravel())
        self._eig_faces = numpy.array(self._eig_faces)

    def _save_vector(self, vector, filename):
        vector = numpy.array(vector)
        (a,b) = (b,a) = self._image_size
        vector.shape = (a,b)
        uint_vector = self._normalize(numpy.array(vector, dtype='uint8'))
        image = Image.fromarray(uint_vector.astype('uint8'))
        image.save(filename)

    def _save_eig_face_images(self):
        for i, eig_face in enumerate(self._eig_faces):
            self._save_vector(eig_face, 'eig-face-%d.tiff' % i)
   
    def project_to_face_space(self, image_path):
        face_img = Image.open(image_path)
        face_data = numpy.array(face_img, dtype='float_').ravel()
        face_data_diff = face_data - self._average_face_data
        face_data_diff = numpy.matrix(face_data_diff)
        face_space_face = face_data_diff * self._eig_faces.T
        return face_space_face
         
    def _normalize(self, vector):
        return vector / numpy.trace((numpy.dot(vector, vector.T)))

    def _lift_to_image_space(self, face_space_face):
        faces = []
        face_space_face = numpy.array(face_space_face)
        eig_t = self._eig_faces[0].T
        for i in range(self._number_of_eig_faces):
            faces.append(eig_t[i] * face_space_face[0][i])
        face_image = reduce(lambda x, y: x + y, faces)
        return face_image + self._average_face_data


    def get_eigen_face_for_image(self, image_path):
        face_space_face = self.project_to_face_space(image_path)
        face_image = self._lift_to_image_space(face_space_face)
        self._save_vector(face_image, 'eigen-eigs.jpg')


class KnnClassifier(object):
    def __init__(self, k, train_data, test_data, eigface):
        self.k = k
        self._train = train_data
        self._test = test_data
        self._eig_face = eigface
        self.lock = Lock()

    def train(self):
        self._eig_face.create_eig_faces(self._train.data)
        self._labelled_face_space_faces = []
        for (face, label) in self._train.labelled_data:
            face_space_face = self._eig_face.project_to_face_space(face)
            self._labelled_face_space_faces.append((face_space_face, label))

    def test(self):
        results = []
        for (face, label) in self._test.labelled_data:
            prediction = self.knn(face)
            result = label <= (prediction + 0.5) and label >= (prediction - 0.5)
            results.append((label, prediction, result))
        return results

    def output_labelled_face_space_faces(self, file_name):
        """outputs a file with a given name containing data in format label,
        dimension, value""" 
        output = []
        for face_space_face, label in self._labelled_face_space_faces:
            face_space_face = face_space_face.tolist()[0]
            for i, value in enumerate(face_space_face):
                output.append((label,i, value))     
        with open(file_name, 'w') as output_file:
            for (label, i, value) in output:
                output_file.write('%s %d %f\n' % (label, i, value))

    def knn(self, face):
        test_face_space_face = self._eig_face.project_to_face_space(face)
        self.distances = []
        thread_pool = ThreadPool(2)
        for (face_space_face, label) in self._labelled_face_space_faces:
            thread_pool.queue_task(self.calculate_distance,
                                   args=(test_face_space_face, 
                                         face_space_face, 
                                         label))
        thread_pool.join_all(wait_for_threads=False)
        self.distances.sort()
        self.distances.reverse()
        k_nearest = self.distances[:self.k]
        k_nearest_labels = map(lambda x: x[1], k_nearest)
        nearest_neighbour = max(set(k_nearest_labels), 
                                key=k_nearest_labels.count)
        return nearest_neighbour

    def calculate_distance(self, test_face_space_face, face_space_face, label):
        distance = self.euclidean_distance(test_face_space_face, face_space_face)
        with self.lock:
            self.distances.append((distance, label))

    def euclidean_distance(self, x, y):
        x_len = len(x)
        y_len = len(y)
        if len(x) != len(y):
            raise ValueError("x and y must be of the same length, x length:\
                    %d\t y length: %d" % (x_len, y_len))
        pairs = zip(x, y)
        pairs_arrays = map(
            lambda (a, b): (numpy.array(a).ravel(), numpy.array(b).ravel()),
                        pairs)
        squared_diffs = map(lambda (a, b): (a - b) * (a - b), pairs_arrays)
        sum_of_squared_diffs = reduce(lambda a, b: a + b, squared_diffs[0])
        return math.sqrt(sum_of_squared_diffs)        
  

class Data(object):
    def __init__(self, data, labels):
        self.data = data
        self.labelled_data = zip(data,labels)
        


def labels_from_csv(image_dir, csv_file):
    """ Assumes csv is in name,score,[train|test] format """
    training_data = []
    training_labels = []
    testing_data = []
    testing_labels = []
    with open(csv_file, 'r') as csv_file:
        for row in csv.reader(csv_file):
            score = float(row[1])
            if score < 0.0:
                label = 'not'
            else:
                label = 'hot'
            image_path = os.path.join(image_dir, row[0])
            if row[2] == 'train':
                training_data.append(image_path)
                training_labels.append(score)#label)
            elif row[2] == 'test':
                testing_data.append(image_path)
                testing_labels.append(score)#label)
            else:
                raise ValueError('csv row did not contain train or test')
    print 'training hot: ', training_labels.count('hot')
    print 'training not: ', training_labels.count('not')
    print 'testing hot: ', testing_labels.count('hot')
    print 'testing not: ', testing_labels.count('not')
    return Data(training_data, training_labels), Data(testing_data, testing_labels) 


def data_from_dir(dir_name):
    data = []
    for file_name in os.listdir(dir_name):
        data.append(os.path.join(dir_name, file_name))
    return data 

def test(knn_classifier):
    numbers = range(100)
    print 'testing'
    odds = numbers[1::2]
    totals = []
    for k in odds:
        knn_classifier.k = k
        results = knn_classifier.test()
        correct = map(lambda (a, b, c): c, results).count(True)
        result = (correct / len(results)) * 100
        print 'accuracy for k=%d:\t%f%%' % (k, result)
        totals.append((result, k))
    print max(results)


def main():
    parser = argparse.ArgumentParser(description="EigFace creates eigenfaces", 
                                epilog="Created by Lloyd Henning for his 3rd \
                                        year project at the Univesity of \
                                        Manchester")
    parser.add_argument('--output-test-file', const='knn-output.txt', nargs='?')
    parser.add_argument('--no-test', default=True, dest='test', action='store_false')
    parser.add_argument('--number-of-eig-faces', default=50, type=int) 
    parser.add_argument('csv_file')
    parser.add_argument('image_dir')
    print parser
    args = parser.parse_args()  

    training_data, testing_data = labels_from_csv(args.image_dir, args.csv_file)
    print 'creating eigenface'
    eig_face = EigFace(number_of_eig_faces=args.number_of_eig_faces)   
    print 'creating knnclasifier'
    knn_classifier = KnnClassifier(1, training_data, testing_data, eig_face)    
    knn_classifier.train()
    if args.output_test_file:
        knn_classifier.output_labelled_face_space_faces(args.output_test_file)
    if args.test:
        test(knn_classifier)

 
if __name__ == '__main__':
    main()
        
