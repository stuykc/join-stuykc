import urllib, urllib2
import logging
from google.appengine.ext import ndb
from models import *

def add_member(name, stuy_id, email):
    config = ndb.Key(Settings, 'config').get()
    if not config:
        config = Settings(id='config')

    new_member = {
            config.name: name,
            config.stuy_id: stuy_id,
            config.email: email
    }
    data = urllib.urlencode(new_member)
    request = urllib2.Request(config.url, data)
    response = urllib2.urlopen(request)
    content = response.read()
    if "Your response has been recorded." in content:
        logging.info("New Member: %s, %s, %s" % (name, stuy_id, email))
        return True
    else:
        return False

