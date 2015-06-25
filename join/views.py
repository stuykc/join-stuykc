from google.appengine.ext import ndb
from join import *
from members import add_member
from models import *
from settings import SettingsHandler

class MainPage(BaseHandler):

    def get(self):
        self.render_template('index.html')

class JoinFormHandler(BaseHandler):

    def get(self):
        self.render_template('join.html')

class SubmitHandler(BaseHandler):

    def post(self):
        name = self.request.get('name')
        stuy_id = self.request.get('id')
        email = self.request.get('email')
        add_member(name, stuy_id, email)

        template_values = {
            'email': email
        }
        self.render_template('submit.html', template_values)

application = webapp2.WSGIApplication([
    ('/admin/settings', SettingsHandler),
    ('/main', MainPage),
    ('/submit', SubmitHandler),
    ('/.*', JoinFormHandler)
], debug=True)
