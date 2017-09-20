from join import *
from members import add_member, send_email

class SubmitHandler(BaseHandler):

    def post(self):
        name = self.request.get('name')
        email = self.request.get('email')
        status = self.request.get('status')
        stuy_id = self.request.get('id')
        osis = self.request.get('osis')
        phone = self.request.get('phone')
        homeroom = self.request.get('homeroom')
        grade = self.request.get('grade')
        success = add_member(name, stuy_id, email,status,osis,phone,homeroom,grade)
        #while not success:
        #    success = add_member(name, stuy_id, email,status,osis,phone,homeroom,grade)
        send_email(name, stuy_id, email,status,osis,phone,homeroom,grade)

        template_values = {
            'email': email
        }
        self.render_template('submit.html', template_values)
