import webapp2
import jinja2
import os
<<<<<<< HEAD

=======
from google.appengine.api import users
import models
>>>>>>> 1276c2721402390c73e2f29ae3a0b5d290e99f2d

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)



class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
<<<<<<< HEAD
        template = jinja_env.get_template("/templates/index.html")
=======
        template = jinja_env.get_template("templates/index.html")
>>>>>>> 1276c2721402390c73e2f29ae3a0b5d290e99f2d
        self.response.write(template.render())


class AddEventPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_env.get_template("templates/addevent.html")
        self.response.write(template.render())




app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/addevent', AddEventPage),
], debug=True)
