from google.appengine.ext import ndb

class BlogPost(ndb.Model):
    title = ndb.StringProperty()
    content = ndb.StringProperty()
    name = ndb.StringProperty()
