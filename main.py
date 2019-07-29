import webapp2
from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.api import images
from google.appengine.api import search
import urllib

import jinja2
import os
import time
import datetime

from models import Event
from models import User






def create_calendar_url(event):
    date = datetime.datetime.strptime(event.event_date, '%Y-%m-%d').strftime('%Y%m%d')
    time = datetime.datetime.strptime(event.event_time, '%H:%M')
    start_time = time.strftime('%H%M%S')
    if start_time > 220000:
        end_time = (time +datetime.timedelta(hours = 0.25)).strftime('%H%M%S')
    else:
        end_time = (time + datetime.timedelta(hours = 2)).strftime('%H%M%S')
    date_and_time = date + 'T' + start_time + '/' + date + 'T' + end_time
    domain = "https://calendar.google.com/calendar/r/eventedit"
    event_details = {
        "text" : event.event_name,
        "dates": date_and_time,
        "details": event.event_des,
        "sf": "true",
        "location": event.event_location,
    }
    data = urllib.urlencode(event_details)
    url = "%s?%s" % (domain, data)
    return url

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
        email_address = None
        if user:
            email_address = user.nickname()
        login_url = users.create_login_url('/main')
        template_vars = {
            "isUser": user,
            "email": email_address,
            "login_url": login_url,
            }
        self.response.write(template.render(template_vars))



    def post(self):
        template = jinja_env.get_template('/templates/index.html')

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_env.get_template("/templates/index.html")
        user = users.get_current_user()
        logout_url = None
        logout_url = users.create_logout_url('/')
        template_vars = {
            "logout_url" : logout_url,
        }
        self.response.write(template.render(template_vars))

class AddEventPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_env.get_template("templates/addevent.html")

        logout_url = None
        logout_url = users.create_logout_url('/')
        template_vars = {
            "logout_url" : logout_url,
        }
        self.response.write(template.render(template_vars))
    def post(self):
        host_name = self.request.get("host_name")
        event_name = self.request.get("event_name")
        event_time = self.request.get("event_time")
        event_location = self.request.get("event_location")
        event_type = self.request.get("event_type")
        event_des = self.request.get("event_des")
        host_email = self.request.get("host_email")
        event_date = self.request.get("event_date")
        date_and_time = datetime.datetime.now()
        optional_image = self.request.get("optional_image")

        event_image = None

        if optional_image == 'on':
            event_image = self.request.get("event_image")





        event_post = Event(host_name=host_name, event_name=event_name, event_date=event_date, event_time=event_time,
        event_location=event_location, event_des=event_des, host_email=host_email, event_type=event_type, optional_image=optional_image,
        event_image=event_image, date_and_time=date_and_time)
        event_post.put()




        if event_type == "sports":
            self.redirect('/sports')
            time.sleep(.5)
        elif event_type == "clubs":
            self.redirect('/clubs')
            time.sleep(.5)
        elif event_type == "academics":
            self.redirect('/academics')
            time.sleep(.5)
        else:
            self.redirect('/socialevents')
            time.sleep(.5)



class SportsPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        sports_events = Event.query(Event.event_type=='sports').order(Event.event_date).order(Event.event_time).fetch()

        logout_url = None
        logout_url = users.create_logout_url('/')


        url_list = []
        for event in sports_events:
            url_name = create_calendar_url(event)
            url_list.append(url_name)



        template_vars = {
            "sports_events":sports_events,
            "url_list": url_list,
            "logout_url" : logout_url,
            }

        template = jinja_env.get_template("templates/sports.html")
        self.response.write(template.render(template_vars))

    def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        sort_button = self.request.get('sort-button')


        if sort_button == 'alphabetical':
            sports_events = Event.query(Event.event_type=='sports').order(Event.event_name).fetch()
        elif sort_button == 'time-of-event':
            sports_events = Event.query(Event.event_type=='sports').order(Event.event_date).order(Event.event_time).fetch()
        elif sort_button == 'time-of-post':
            sports_events = Event.query(Event.event_type=='sports').order(-Event.date_and_time).fetch()
        elif sort_button == 'number-of-people':
            sports_events = Event.query(Event.event_type=='sports').order(-Event.num_attendees).fetch()



        logout_url = None
        logout_url = users.create_logout_url('/')


        url_list = []
        for event in sports_events:
            url_name = create_calendar_url(event)
            url_list.append(url_name)



        template_vars = {
            "sports_events":sports_events,
            "url_list": url_list,
            "logout_url" : logout_url,
            }

        template = jinja_env.get_template("templates/sports.html")
        self.response.write(template.render(template_vars))


class AcademicsPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'

        academics_events = Event.query(Event.event_type=='academics').order(Event.event_date).order(Event.event_time).fetch()


        logout_url = None
        logout_url = users.create_logout_url('/')

        url_list = []
        for event in academics_events:
            url_name = create_calendar_url(event)
            url_list.append(url_name)

        template_vars = {
            "academics_events":academics_events,
            "url_list": url_list,
            "logout_url" : logout_url,
            }
        template = jinja_env.get_template("/templates/academics.html")
        self.response.write(template.render(template_vars))
    def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        sort_button = self.request.get('sort-button')

        if sort_button == 'alphabetical':
            academics_events = Event.query(Event.event_type=='academics').order(Event.event_name).fetch()
        elif sort_button == 'time-of-event':
            academics_events = Event.query(Event.event_type=='academics').order(Event.event_date).order(Event.event_time).fetch()
        elif sort_button == 'time-of-post':
            academics_events = Event.query(Event.event_type=='academics').order(-Event.date_and_time).fetch()
        elif sort_button == 'number-of-people':
            academics_events = Event.query(Event.event_type=='academics').order(-Event.num_attendees).fetch()

        logout_url = None
        logout_url = users.create_logout_url('/')


        url_list = []
        for event in academics_events:
            url_name = create_calendar_url(event)
            url_list.append(url_name)



        template_vars = {
            "academics_events":academics_events,
            "url_list": url_list,
            "logout_url" : logout_url,
            }

        template = jinja_env.get_template("templates/academics.html")
        self.response.write(template.render(template_vars))


class ClubsPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        clubs_events = Event.query(Event.event_type=='clubs').order(Event.event_date).order(Event.event_time).fetch()

        logout_url = None
        logout_url = users.create_logout_url('/')

        url_list = []
        for event in clubs_events:
            url_name = create_calendar_url(event)
            url_list.append(url_name)

        template_vars = {
            "clubs_events":clubs_events,
            "url_list": url_list,
            "logout_url" : logout_url,
            }

        template = jinja_env.get_template("/templates/clubs.html")
        self.response.write(template.render(template_vars))

    def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        sort_button = self.request.get('sort-button')

        if sort_button == 'alphabetical':
            clubs_events = Event.query(Event.event_type=='clubs').order(Event.event_name).fetch()
        elif sort_button == 'time-of-event':
            clubs_events = Event.query(Event.event_type=='clubs').order(Event.event_date).order(Event.event_time).fetch()
        elif sort_button == 'time-of-post':
            clubs_events = Event.query(Event.event_type=='clubs').order(-Event.date_and_time).fetch()
        elif sort_button == 'number-of-people':
            clubs_events = Event.query(Event.event_type=='clubs').order(-Event.num_attendees).fetch()

        logout_url = None
        logout_url = users.create_logout_url('/')


        url_list = []
        for event in clubs_events:
            url_name = create_calendar_url(event)
            url_list.append(url_name)



        template_vars = {
            "clubs_events":clubs_events,
            "url_list": url_list,
            "logout_url" : logout_url,
            }

        template = jinja_env.get_template("templates/clubs.html")
        self.response.write(template.render(template_vars))


class SocialEventsPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        social_events = Event.query(Event.event_type=='parties').order(Event.event_date).order(Event.event_time).fetch()

        logout_url = None
        logout_url = users.create_logout_url('/')

        url_list = []
        for event in social_events:
            url_name = create_calendar_url(event)
            url_list.append(url_name)

        template_vars = {
            "social_events":social_events,
            "url_list": url_list,
            "logout_url" : logout_url,
            }
        template = jinja_env.get_template("/templates/socialevents.html")
        self.response.write(template.render(template_vars))
    def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        sort_button = self.request.get('sort-button')

        if sort_button == 'alphabetical':
            social_events = Event.query(Event.event_type=='parties').order(Event.event_name).fetch()
        elif sort_button == 'time-of-event':
            social_events = Event.query(Event.event_type=='parties').order(Event.event_date).order(Event.event_time).fetch()
        elif sort_button == 'time-of-post':
            social_events = Event.query(Event.event_type=='parties').order(-Event.date_and_time).fetch()
        elif sort_button == 'number-of-people':
            social_events = Event.query(Event.event_type=='parties').order(-Event.num_attendees).fetch()

        logout_url = None
        logout_url = users.create_logout_url('/')


        url_list = []
        for event in social_events:
            url_name = create_calendar_url(event)
            url_list.append(url_name)



        template_vars = {
            "social_events":social_events,
            "url_list": url_list,
            "logout_url" : logout_url,
            }

        template = jinja_env.get_template("templates/socialevents.html")
        self.response.write(template.render(template_vars))

class CounterHandler(webapp2.RequestHandler):
    def post(self):
        event_key = self.request.get('event_key')
        event_key = ndb.Key(urlsafe=event_key)
        event = event_key.get()
        event.num_attendees += 1
        event.put()
        user = users.get_current_user()
        attendee = User.query(User.email == user.nickname()).get()
        if attendee and event not in attendee.events:
            attendee.events.append(event_key)
            attendee.put()
        else:
            attendee = User(email = user.nickname(), events = [event_key])
            attendee.put()

class SubtractHandler(webapp2.RequestHandler):
    def post(self):
        event_key = self.request.get('event_key')
        event_key = ndb.Key(urlsafe=event_key)
        event = event_key.get()
        event.num_attendees -= 1
        event.put()
        user = users.get_current_user()
        attendee = User.query(User.email == user.nickname()).get()
        if attendee:
            attendee.events.remove(event_key)
            attendee.put()



class YourEventsPage(webapp2.RequestHandler):
    def get(self):

        template = jinja_env.get_template("/templates/yourevents.html")
        self.response.headers['Content-Type'] = 'text/html'
        user = users.get_current_user()
        user_email = user.nickname()
        attendee = User.query(User.email == user_email).get()
        events = []
        if attendee:
            for event_key in attendee.events:
                events.append(event_key.get())
        logout_url = None
        logout_url = users.create_logout_url('/')
        template_vars = {
            "logout_url" : logout_url,
            "events": events,
        }



        self.response.write(template.render(template_vars))
    def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        sort_button = self.request.get('sort-button')

        if sort_button == 'alphabetical':
            events = Event.query().order(Event.event_name).fetch()
        elif sort_button == 'time-of-event':
            events = Event.query().order(Event.event_date).order(Event.event_time).fetch()
        elif sort_button == 'time-of-post':
            events = Event.query().order(-Event.date_and_time).fetch()
        elif sort_button == 'number-of-people':
            events = Event.query().order(-Event.num_attendees).fetch()

        logout_url = None
        logout_url = users.create_logout_url('/')

        template_vars = {
            "events":events,
            "logout_url" : logout_url,
            }

        template = jinja_env.get_template("templates/yourevents.html")
        self.response.write(template.render(template_vars))


class Image(webapp2.RequestHandler):
    def get(self):
        event_key = ndb.Key(urlsafe=self.request.get('event_key'))
        event = event_key.get()
        if event.event_image:
            self.response.headers['Content-Type'] = 'image/png'
            self.response.out.write(event.event_image)

class AboutUs(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template("/templates/aboutus.html")
        self.response.headers['Content-Type'] = 'text/html'

        logout_url = None
        logout_url = users.create_logout_url('/')

        template_vars = {

            "logout_url" : logout_url,
            }
        self.response.write(template.render(template_vars))

class SearchPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template("/templates/search.html")
        self.response.headers['Content-Type'] = 'text/html'
        search_bar = self.request.get("search-bar")

        logout_url = None
        logout_url = users.create_logout_url('/')

        template_vars = {
            "logout_url":logout_url,
        }

        self.response.write(template.render(template_vars))
    def post(self):
        template = jinja_env.get_template("/templates/search.html")
        self.response.headers['Content-Type'] = 'text/html'
        search_bar = self.request.get("search-bar")

        logout_url = None
        logout_url = users.create_logout_url('/')

        template_vars = {
            "logout_url":logout_url,
        }

        self.response.write(template.render(template_vars))
class SearchResults(webapp2.RequestHandler):
    def post(self):
        self.response.headers['Content-Type'] = 'text/html'
        search_bar = self.request.get("search-bar")
        event_search_results = Event.query(Event.event_name == search_bar).fetch()
        name_search_results = Event.query(Event.host_name == search_bar).fetch()
        date_search_results = Event.query(Event.event_date == search_bar).fetch()
        location_search_results = Event.query(Event.event_location == search_bar).fetch()
        search_results = event_search_results + name_search_results + date_search_results + location_search_results



        logout_url = None
        logout_url = users.create_logout_url('/')

        url_list = []
        for event in search_results:
            url_name = create_calendar_url(event)
            url_list.append(url_name)

        template_vars = {
            "search_results":search_results,
            "url_list": url_list,
            "logout_url" : logout_url,
            }
        template = jinja_env.get_template("/templates/searchresults.html")
        self.response.write(template.render(template_vars))



app = webapp2.WSGIApplication([
    ('/', IntroPage),
    ('/main', MainPage),
    ('/addevent', AddEventPage),
    ('/sports', SportsPage),
    ('/academics', AcademicsPage),
    ('/clubs', ClubsPage),
    ('/socialevents', SocialEventsPage),
    ('/yourevents', YourEventsPage),
    ('/counter', CounterHandler),
    ('/subtract', SubtractHandler),
    ('/image', Image),
    ('/aboutus', AboutUs),
    ('/search', SearchPage),
    ('/searchresults', SearchResults),

], debug=True)
