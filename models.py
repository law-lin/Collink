from google.appengine.ext import ndb

class Event(ndb.Model):
    host_name = ndb.StringProperty()
    event_name = ndb.StringProperty()
    event_time = ndb.StringProperty()
    event_date = ndb.StringProperty()
    event_location = ndb.StringProperty()
    event_des = ndb.TextProperty()
    host_email = ndb.StringProperty()
    event_type = ndb.StringProperty()
    num_attendees = ndb.IntegerProperty(default=0)

class User(ndb.Model):
    email = ndb.StringProperty()
    events = ndb.KeyProperty(repeated=True)
