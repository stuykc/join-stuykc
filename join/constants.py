from join.models import *
from google.appengine.ext import ndb

config = ndb.Key(Settings, 'config').get()
if not config:
    config = Settings(id='config')

config.put()
