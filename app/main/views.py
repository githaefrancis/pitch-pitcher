
from flask import redirect, render_template, url_for
from flask_login import current_user, login_required
from . import main
from .forms import PitchForm,CommentForm
from ..models import Category, Comment, Pitch

from .request import get_all_comments, get_all_downvotes, get_all_upvotes

@main.route('/',methods=['GET'])
def index():
  pitch_form=PitchForm()

  pitches=Pitch.query.order_by(Pitch.id.desc()).all()
  comments=get_all_comments(pitches)
  upvotes=get_all_upvotes(pitches)
  downvotes=get_all_downvotes(pitches)
  return render_template('index.html',pitch_form=pitch_form,pitches=pitches,comments=comments,upvotes=upvotes,downvotes=downvotes)

# @main.route('/user/<user_name>')
# def profile(user_name):
#   return '<h1> Hello</h1>'


@main.route('/',methods=['POST'])
@login_required
def post():
  pitch_form=PitchForm()

  if pitch_form.validate_on_submit():
    new_pitch=Pitch(category=Category.query.filter_by(name=pitch_form.category.data).first(),content=pitch_form.content.data,user=current_user)
    new_pitch.save_pitch()
    return redirect(url_for('main.index'))

@main.route('/pitch/<pitch_id>',methods=['GET'])
def single_pitch(pitch_id):
  comment_form=CommentForm()
  pitch=Pitch.query.filter_by(id=pitch_id).first()
  comments_list=Comment.query.filter_by(pitch=pitch).order_by(Comment.id.desc()).all()
  return render_template('pitch.html',pitch=pitch,comment_form=comment_form,comments=comments_list)

@main.route('/pitch/<pitch_id>',methods=['POST'])
@login_required
def comment(pitch_id):
  comment_form=CommentForm()
  pitch=Pitch.query.filter_by(id=pitch_id).first()
  if comment_form.validate_on_submit():
    comment=Comment(user=current_user,pitch=pitch,content=comment_form.comment.data)
    comment.save_comment()
    
    return redirect(url_for('main.single_pitch',pitch_id=pitch_id))


@main.route('/user/profile')
@login_required
def profile():
  my_pitches=Pitch.query.filter_by(user=current_user).order_by(Pitch.id.desc()).all()
  comments=get_all_comments(my_pitches)
  upvotes=get_all_upvotes(my_pitches)
  downvotes=get_all_downvotes(my_pitches)
  return render_template('index.html',pitches=my_pitches,user=current_user,comments=comments,upvotes=upvotes,downvotes=downvotes)
  # return render_template('profile/profile.html',user=current_user,pitches=my_pitches)