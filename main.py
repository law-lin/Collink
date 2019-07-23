import webapp2
from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import os

import models


jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class IntroPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_env.get_template("/templates/intropage.html")
        self.response.write(template.render())



class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_env.get_template("/templates/index.html")
        self.response.write(template.render())




class AddEventPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_env.get_template("templates/addevent.html")
        self.response.write(template.render())


app = webapp2.WSGIApplication([
    ('/', IntroPage),
    ('/main', MainPage),
    ('/addevent', AddEventPage),
], debug=True)
