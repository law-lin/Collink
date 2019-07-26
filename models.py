from google.appengine.ext import ndb

<<<<<<< HEAD
class User(ndb.Model):
    email = ndb.StringProperty()
    events = ndb.KeyProperty(repeated = True)

=======
>>>>>>> 86711737c1874b9c8bf55bdd4cf622164a51ff4f
class Event(ndb.Model):
    host_name = ndb.StringProperty()
    event_name = ndb.StringProperty()
    event_time = ndb.StringProperty()
    event_date = ndb.StringProperty()
    event_location = ndb.StringProperty()
    event_des = ndb.TextProperty()
    event_image = ndb.BlobProperty()
    host_email = ndb.StringProperty()
    event_type = ndb.StringProperty()
    num_attendees = ndb.IntegerProperty(default=0)
<<<<<<< HEAD
=======

class User(ndb.Model):
    email = ndb.StringProperty()
    events = ndb.KeyProperty(repeated=True)
>>>>>>> 86711737c1874b9c8bf55bdd4cf622164a51ff4f
