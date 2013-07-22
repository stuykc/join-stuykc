from flask import render_template, flash, redirect, url_for, request
from app import app
from add import add_member

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        add_member(request.form['name'], request.form['id'], request.form['email'])
        flash(request.form['email'])
        return redirect(url_for('join'))
    else:
        return render_template('index.html')

@app.route('/join')
def join():
    return render_template('join.html')
