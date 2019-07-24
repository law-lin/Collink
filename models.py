from google.appengine.ext import ndb

class CollegeStudent(ndb.Model):
    name = ndb.StringProperty()
    collegename = ndb.StringProperty()
    classyear = ndb.IntegerProperty()

class Event(ndb.Model):
    host_name = ndb.StringProperty()
    event_name = ndb.StringProperty()
    event_time = ndb.StringProperty()
    event_location = ndb.StringProperty()
    event_des = ndb.TextProperty()
    host_email = ndb.StringProperty()
    event_type = ndb.StringProperty()
