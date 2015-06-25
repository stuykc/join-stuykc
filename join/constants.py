from google.appengine.ext import ndb
from join.models import *

config = ndb.Key(Settings, 'config').get()
if not config:
    config = Settings(id='config')

config.put()
