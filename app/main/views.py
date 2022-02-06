from flask import render_template
from . import main


@main.route('/')
def index():
  return render_template('index.html')

@main.route('/user/<user_name>')
def profile(user_name):
  return '<h1> Hello</h1>'