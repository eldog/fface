from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import logging

import numpy
import theano
import theano.tensor as T

from utils import get_pickle, save_pickle

class EigenFace(object):
    """Calculated the eigenfaces of a given set of faces"""

    def __init__(self, faces, n_eigs=100, face_space=None):
        """
        Create the facespace of a given set of faces.

        :type faces: numpy.ndarray
        :param faces: an n x m dimensional array off face image data

        :type n_eigs: int
        :param n_eigs: the number of dimensions that the facespace should
                       have. It will be a n_eigs x m dimensional array.

        :type data_file_name: str
        :param data_file_name: the name of the data file that can be used
                               to load a previously calculated facespace
        """
        self.n_eigs = n_eigs
        logging.debug('using %d eigenfaces' % self.n_eigs)
        # convert face data to correct type for theano to use gpu
        faces = numpy.asarray(faces, dtype=theano.config.floatX)
        # calculate the mean face, Psi
        logging.info('calculating mean face')
        self.mean_face = faces.mean(axis=1)
        if face_space is None:
            face_space = self._create_face_space(faces)
        self.entire_face_space = face_space
        self.face_space = face_space[:,:self.n_eigs]

    def _create_face_space(self, faces):
        # create the face space, i.e., the eigenvectors of the faces
        face_diffs = (faces.T - self.mean_face).T
        x = T.matrix()
        covar = T.dot(x.T, x)
        f_covar = theano.function([x], covar) 
        logging.info('calculating covariance matrix')
        sigma = f_covar(face_diffs)
        logging.info('performing singular value decomposition')
        u, s, v = numpy.linalg.svd(sigma)
        # take the first n_eigs eigenfaces for facespace
        logging.info('creating facespace')
        return numpy.dot(face_diffs, u)

    @classmethod
    def from_file(cls, faces, data_file_name, n_eigs):
        pickle = get_pickle(data_file_name)
        if pickle is not None:
            logging.info('using previously calculated facespace')
            return cls(faces, n_eigs=n_eigs, face_space=pickle)
        else:
            logging.info('No previous facespace was found')
            eig_face = cls(faces, n_eigs=n_eigs)
            save_pickle(eig_face.entire_face_space, data_file_name)
            return eig_face

    def project_to_face_space(self, faces):
        """
        Returns a set of faces projected into the face space

        :type faces: numpy.ndarray
        :param faces: an n x p dimensional array of face image data
        """
        f_spaced_faces = []
        for face in faces.T:
            face_diff = face - self.mean_face
            f_spaced_faces.append(numpy.dot(self.face_space.T, face_diff))
        return numpy.asarray(f_spaced_faces).T

