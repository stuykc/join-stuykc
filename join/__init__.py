import os, webapp2, jinja2
from constants import *

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')),
    extensions=['jinja2.ext.autoescape'])

class BaseHandler(webapp2.RequestHandler):

    def render_template(self, template_filename, template_values={}):
        template = JINJA_ENVIRONMENT.get_template(template_filename)
        self.response.out.write(template.render(template_values))
