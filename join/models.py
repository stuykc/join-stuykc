from google.appengine.ext import ndb

class Settings(ndb.Expando):

    url = ndb.StringProperty(default="https://docs.google.com/forms/d/e/1FAIpQLSeilPQbEemJnTv7DV5fLUYlOjGxvcycGrnp7Drob6ela8aicw/formResponse")
    name = ndb.StringProperty(default="entry.1177263284")
    stuy_id = ndb.StringProperty(default="entry.1021359563")
    email = ndb.StringProperty(default="entry.1794511464")
    status = ndb.StringProperty(default="entry.2008265881")
    osis = ndb.StringProperty(default="entry.1993643091")
    phone = ndb.StringProperty(default="entry.1437712310")
    homeroom = ndb.StringProperty(default="entry.1919658451")
    grade = ndb.StringProperty(default="entry.1345015364")
