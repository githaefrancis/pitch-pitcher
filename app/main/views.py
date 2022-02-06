from flask import render_template
from . import main
from .forms import PitchForm

@main.route('/')
def index():
  pitch_form=PitchForm()

  # if pitch_form.validate_on_submit():
  #   new_p

  return render_template('index.html',pitch_form=pitch_form)

@main.route('/user/<user_name>')
def profile(user_name):
  return '<h1> Hello</h1>'