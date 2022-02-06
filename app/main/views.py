from unicodedata import category
from flask import redirect, render_template, url_for
from flask_login import current_user
from . import main
from .forms import PitchForm
from ..models import Category, Pitch

@main.route('/')
def index():
  pitch_form=PitchForm()

  if pitch_form.validate_on_submit():
    redirect(url_for('main.post',pitch_form=pitch_form))

  return render_template('index.html',pitch_form=pitch_form)

@main.route('/user/<user_name>')
def profile(user_name):
  return '<h1> Hello</h1>'

@main.route('/post/new/<pitch_form>',methods=['GET','POST'])
def post(pitch_form):
  new_pitch=Pitch(category=Category.query.filter_by(name=pitch_form.category.data),content=pitch_form.content.data,user=current_user)
