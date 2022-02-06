
from flask import redirect, render_template, url_for
from flask_login import current_user, login_required
from . import main
from .forms import PitchForm
from ..models import Category, Pitch

@main.route('/',methods=['GET'])
def index():
  pitch_form=PitchForm()



  return render_template('index.html',pitch_form=pitch_form)

@main.route('/user/<user_name>')
def profile(user_name):
  return '<h1> Hello</h1>'


@main.route('/',methods=['POST'])
@login_required
def post():
  pitch_form=PitchForm()

  if pitch_form.validate_on_submit():
    new_pitch=Pitch(category=Category.query.filter_by(name=pitch_form.category.data).first(),content=pitch_form.content.data,user=current_user)
    new_pitch.save_pitch()
    return redirect(url_for('main.index'))