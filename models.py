from google.appengine.ext import ndb

class CollegeStudent (ndb.Model):
    name = ndb.StringProperty()
    collegename = ndb.StringProperty()
    classyear = ndb.IntegerProperty()
