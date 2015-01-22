from google.appengine.ext import ndb
from join import *
from join.add import add_member
from join.models import *

class MainPage(BaseHandler):

    def get(self):
        self.render_template('index.html')

class JoinFormHandler(BaseHandler):

    def get(self):
        self.render_template('join.html')

class SubmitHandler(BaseHandler):

    def post(self):
        name = self.request.get('name')
        stuyId = self.request.get('id')
        email = self.request.get('email')
        add_member(name, stuyId, email)

        template_values = {
            'email': email
        }
        self.render_template('submit.html')

class SettingsHandler(BaseHandler):

    def get(self):
        self._serve_page()

    def post(self):
        config = ndb.Key(Settings, 'config').get()
        if not config:
            config = Settings(id='config')

        config.google_username = self.request.get('google_username')
        config.google_password = self.request.get('google_password')

        config.put()
        self._serve_page()

    def _serve_page(self):
        config_key = ndb.Key(Settings, 'config')
        if config_key:
            config = config_key.get()
        else:
            config = {}

        template_values = {
            'config': config
        }
        self.render_template('settings.html', template_values)

application = webapp2.WSGIApplication([
    ('/admin/settings', SettingsHandler),
    ('/main', MainPage),
    ('/submit', SubmitHandler),
    ('/.*', JoinFormHandler)
], debug=True)
