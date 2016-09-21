import urllib, urllib2
import logging
from google.appengine.ext import ndb
from google.appengine.api import mail
from models import *

def add_member(name, stuy_id, email, status, osis, phone, homeroom, grade):
    config = ndb.Key(Settings, 'config').get()
    if not config:
        config = Settings(id='config')

    new_member = {
            config.name: name,
            config.stuy_id: stuy_id,
            config.email: email,
            config.status: status,
            config.osis: osis,
            config.phone: phone,
            config.homeroom: homeroom,
            config.grade: grade
    }
    data = urllib.urlencode(new_member)
    request = urllib2.Request(config.url, data)
    response = urllib2.urlopen(request)
    content = response.read()
    if "Your response has been recorded." in content:
        logging.info("New Member: %s, %s, %s, %s, %s, %s, %s, %s" % (name, stuy_id, email, status, osis, phone, homeroom, grade))
        return True
    else:
        return False

def send_email(name, stuy_id, email, status, osis, phone, homeroom, grade):
    message = mail.EmailMessage(
            sender = "Stuyvesant Key Club <stuyvesantkeyclub@gmail.com>",
            subject = "Thank you for joining Stuyvesant Key Club!"
    )
    message.to = email
    message.body = """
Hey %s,

Thank you for signing up to be a part of Stuyvesant Key Club! We are part of the world's largest high school service organization that exist today! Here, you'll find your passion in volunteering, and developing amazing leadership qualities while having LOTS of fun.

You had submitted the following information:
    Name: %s
    4-Digit ID: %s
    Email: %s
    Membership Status: %s
    9-Digit OSIS: %s
    Phone Number: %s
    Homeroom: %s
    Grade: %s

We hope you join us on our facebook group (https://www.facebook.com/groups/stuyvesantkeyclub/), where we will post important updates and about other awesome news. We also have a mailing list that you should definitely sign up for(https://groups.google.com/forum/#!forum/stuyvesant-key-club)!

See you at our next meeting/event!

Best,
The Stuyvesant Key Club Cabinet
""" % (name, name, stuy_id, email, status, osis, phone, homeroom, grade)
    message.send()
