from datetime import datetime
from google.appengine.ext import ndb
from join.models import *

config = ndb.Key(Settings, 'config').get()
if not config:
    config = Settings(id='config')

# Used for bulk email sending
GOOGLE_USERNAME = "< Google Email >"
GOOGLE_PASSWORD = "< Google Password >"
try:
    GOOGLE_USERNAME = config.google_username
    GOOGLE_PASSWORD = config.google_password
except:
    config.google_username = GOOGLE_USERNAME
    config.google_password = GOOGLE_PASSWORD
GOOGLE_USERNAME = config.google_username
GOOGLE_PASSWORD = config.google_password

config.put()
