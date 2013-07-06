from flask import render_template
from app import app

@app.route('/', methods = ['GET', 'POST'])
def join():
    return render_template("join.html")
