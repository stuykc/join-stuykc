from flask import Flask

app = Flask(__name__)
app.secret_key = 'stuykc_beaver_one_beaver_all_lets_all_do_the_beaver_call'

from app import views, add
