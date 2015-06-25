from join import *
from members import add_member, send_email

class SubmitHandler(BaseHandler):

    def post(self):
        name = self.request.get('name')
        stuy_id = self.request.get('id')
        email = self.request.get('email')
        success = add_member(name, stuy_id, email)
        while not success:
            success = add_member(name, stuy_id, email)
        send_email(name, stuy_id, email)

        template_values = {
            'email': email
        }
        self.render_template('submit.html', template_values)
