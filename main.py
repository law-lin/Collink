import webapp2
import jinja2
import os
from google.appengine.api import users
import models

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)



class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_env.get_template("Collink/templates/index.html")
        self.response.write(template.render())


class AddEventPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_env.get_template("Collink/templates/addevent.html")
        self.response.write(template.render())
    



app = webapp2.WSGIApplication([
    ('/', MainPage)
    ('/', AddEventPage),
], debug=True)
