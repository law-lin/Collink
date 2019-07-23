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
        user = users.get_current_user()
        login_url = None
        logout_url = None
        email_address = None
        if user:
            email_address = user.nickname()
            logout_url = users.create_logout_url('/')
            self.response.write('''
            Welcome to Collink, %s! Select the college you attend! <br>
            <form method="post" action="">Name:
            <input type="text" name="name">College:
            <select name = "College" required = "required">
                <option value = "mit"</option>Massachusetts Institute of Technology
                <option value = "stanford"</option>Stanford University
            </select>
            <input type="submit">
            </form>
            ''' % (email_address))
        else:
            login_url = users.create_login_url('/')
        template_vars = {
                "isUser": user,
                "email": email_address,
                "login_url": login_url,
                "logout_url": logout_url,
                }
        self.response.write(template.render(template_vars))



class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_env.get_template("/templates/index.html")
        self.response.write(template.render())

class MITPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_env.get_template("/templates/index.html")
        self.response.write(template.render())





class StanfordPage(webapp2.RequestHandler):
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
<<<<<<< HEAD
    ('/mit', MITPage),
    ('/stanford', StanfordPage),
=======
>>>>>>> bd8e1ce3276bb2a85b39526596bea8cdc9fe5c1d
    ('/addevent', AddEventPage),
], debug=True)
