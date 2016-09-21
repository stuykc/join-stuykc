from join import *
from google.appengine.ext import ndb

class SettingsHandler(BaseHandler):

    def get(self):
        self._serve_page()

    def post(self):
        config = ndb.Key(Settings, 'config').get()
        if not config:
            config = Settings(id='config')

        config.url = self.request.get('url')
        config.name = self.request.get('name')
        config.stuy_id = self.request.get('stuy_id')
        config.email = self.request.get('email')
        config.status = self.request.get('status')
        config.osis = self.request.get('osis')
        config.phone = self.request.get('phone')
        config.homeroom = self.request.get('homeroom')
        config.grade = self.request.get('grade')

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
