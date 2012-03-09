#!/usr/bin/env python2.7

from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import urllib2

register_openers()
datagen, headers = multipart_encode({ 'image' : open('test.jpg', 'rb'),
                                       'id' : 3})

request = urllib2.Request('http://localhost:8080/upload', datagen, headers)

print urllib2.urlopen(request).read()

