from join import *
from settings import SettingsHandler
from submit import SubmitHandler

class MainPage(BaseHandler):

    def get(self):
        self.render_template('index.html')

class JoinFormHandler(BaseHandler):

    def get(self):
        self.render_template('join.html')

application = webapp2.WSGIApplication([
    ('/admin/settings', SettingsHandler),
    ('/main', MainPage),
    ('/submit', SubmitHandler),
    ('/.*', JoinFormHandler)
], debug=True)
