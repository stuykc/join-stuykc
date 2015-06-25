from join import *
from members import add_member

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


