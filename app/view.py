from app import app
from flask import render_template


@app.route('/')
def index():
    name = 'Lol'
    return render_template('index.html', name=name)


@app.route('/profile')
def profile():
    name = 'Sergey'
    return render_template('profile.html', name=name)