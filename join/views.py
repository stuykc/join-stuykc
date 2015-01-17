import os, webapp2, jinja2
from add import add_member

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')),
    extensions=['jinja2.ext.autoescape'])

class MainPage(webapp2.RequestHandler):

    def get(self):
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render({}))

class JoinFormHandler(webapp2.RequestHandler):

    def get(self):
        template = JINJA_ENVIRONMENT.get_template('join.html')
        self.response.write(template.render({}))

class SubmitHandler(webapp2.RequestHandler):

    def post(self):
        name = self.request.get('name')
        stuyId = self.request.get('id')
        email = self.request.get('email')

        add_member(name, stuyId, email)

        template_values = {
            'email': email
        }

        template = JINJA_ENVIRONMENT.get_template('submit.html')
        self.response.write(template.render(template_values))

application = webapp2.WSGIApplication([
    ('/main', MainPage),
    ('/submit', SubmitHandler),
    ('/.*', JoinFormHandler)
], debug=True)
