#!/usr/bin/env python2.5

import cgi
import datetime
import os
import urllib
import wsgiref.handlers

from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

def template_path(name, template_values):
    path = os.path.join(os.path.dirname(__file__), name)
    return template.render(path, template_values)

class Face(db.Model):
    image = db.BlobProperty()
    score = db.FloatProperty()
    data = db.DateTimeProperty(auto_now_add=True)
    number_of_votes = db.IntergerProperty(default=0)

class FaceVote(db.Model):
    voter = db.UserProperty()
    face_a = db.ReferenceProperty(Face, collection_name="face_a")
    face_b = db.ReferenceProperty(Face, collection_name="face_b")
    a_hotter = db.BooleanProperty()
    date = db.DateTimeProperty(auto_now_add=True)

class MainPage(webapp.RequestHandler):
    def get(self):
        self.get_pictures()
        template_values = {}
        self.response.out.write(template_path('index.html', template_values))

    def post(self):
        self.save()
        self.get_pictures()

    def get_pictures(self):
        pass

    def save(self):
        pass

class UploadPage(webapp.RequestHandler):
    def get(self):
        template_values = {}
        self.response.out.write(template_path('upload.html', template_values))
    def post(self):
        key = self.request.get('id')
        face = Face(key_name=key)
        image = self.request.get('image')
        face.image = db.Blob(image)
        face.put()
        template_values = { 'uploaded' : 'image uploaded' }
        self.response.out.write(template_path('upload.html', template_values))

class Image(webapp.RequestHandler):
    def get(self):
        face = Face.get_by_key_name(self.request.get('id'))
        if face.image:
            self.response.headers['Content-Type'] = 'image/jpeg'
            self.response.out.write(face.image)
        else:
            self.error(404)


pages = []
pages.append(('/', MainPage))
pages.append(('/upload', UploadPage))
pages.append(('/img', Image))
application = webapp.WSGIApplication(pages, debug=True)

def main():
    run_wsgi_app(application)

if __name__ == '__main__':
    main()
