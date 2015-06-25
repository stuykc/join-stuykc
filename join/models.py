from google.appengine.ext import ndb

class Settings(ndb.Expando):

    url = ndb.StringProperty(default="https://docs.google.com/forms/d/1twBY3SCHBcOGyL02jXlZX9VCvNwoxl01ekJMRq1Uw4w/formResponse")
    name = ndb.StringProperty(default="entry.1920483009")
    stuy_id = ndb.StringProperty(default="entry.1400765512")
    email = ndb.StringProperty(default="entry.96846041")
