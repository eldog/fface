#!/usr/bin/env python2.7
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from argparse import ArgumentParser
import os
import sys

import Image
import numpy
import pylab
import theano
from theano.tensor.nnet import conv
import theano.tensor as T
from theano.tensor.signal import downsample


def max_pool(face_file_name):
    input = T.matrix(name='input')
    max_pool_shape = (2,2)
    pool_out = downsample.max_pool_2d(input, max_pool_shape, ignore_border=True)
    f = theano.function([input], pool_out)
    
    img = Image.open(face_file_name) 
    img = numpy.asarray(img, dtype='float32') / 256
    img= img[:,:,1]
    
    img_convolved = f(img)

    pylab.imshow(img_convolved)
    pylab.show()


def filter_face(face_file_name):
    rng = numpy.random.RandomState(45678)
    input = T.tensor4(name='input')

    w_shp = (2, 3, 9, 9)
    w_bound = numpy.sqrt(3 * 9 * 9)
    W = theano.shared(numpy.asarray
                        (rng.uniform(
                            low=-1.0 / w_bound, 
                            high=1.0 / w_bound,
                            size=w_shp),
                            dtype=input.dtype), name='W')

    b_shape = (2,)
    b = theano.shared(numpy.asarray(
                    rng.uniform(
                        low=-.5,
                        high=.5,
                        size=b_shape),
                        dtype=input.dtype),
                        name='b')
    conv_out = conv.conv2d(input, W)

    output = T.nnet.sigmoid(conv_out + b.dimshuffle('x', 0, 'x', 'x'))

    f = theano.function([input], output)

    img = Image.open(face_file_name)

    img = numpy.asarray(img, dtype='float32')/256.

    img_ = img.swapaxes(0,2).swapaxes(1,2).reshape(1,3,128,128)

    filtered_img = f(img_)

    # plot original image and first and second components of output
    pylab.subplot(1,3,1); pylab.axis('off'); pylab.imshow(img)
    pylab.gray();
    # recall that the convOp output (filtered image) is actually a "minibatch",
    # of size 1 here, so we take index 0 in the first dimension:
    pylab.subplot(1,3,2); pylab.axis('off'); pylab.imshow(filtered_img[0,0,:,:])
    pylab.subplot(1,3,3); pylab.axis('off'); pylab.imshow(filtered_img[0,1,:,:])
    pylab.show()

def build_argument_parser():
    argument_parser = ArgumentParser()
    argument_parser.add_argument('--face-file-name',
            default='../../../data/eccv2010_beauty_data/hotornot_face/female_19_RYHZKYB_face_1.jpg')
    return argument_parser

def main(argv=None):
    if argv is None:
        argv = sys.argv
    argument_parser = build_argument_parser()
    args = argument_parser.parse_args(args=argv[1:])
    filter_face(args.face_file_name)
    max_pool(args.face_file_name)

if __name__ == '__main__':
    exit(main())

