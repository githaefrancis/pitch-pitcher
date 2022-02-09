
from flask import redirect, render_template, url_for,request,flash
from flask_login import current_user, login_required
from . import main
from .forms import PitchForm,CommentForm,DownVoteForm
from ..models import Category, Comment, Pitch,Vote,User

from .request import get_all_comments, get_all_downvotes, get_all_upvotes, get_user_votes
from werkzeug.utils import secure_filename
import os

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


@main.route('/',methods=['GET'])
def index():
  pitch_form=PitchForm()
  # downvote_form=DownVoteForm()
  pitches=Pitch.query.order_by(Pitch.id.desc()).all()
  comments=get_all_comments(pitches)
  upvotes=get_all_upvotes(pitches)
  downvotes=get_all_downvotes(pitches)
  if current_user.is_authenticated:
    user_votes=get_user_votes(pitches)
  else:
    user_votes=None
  return render_template('index.html',pitch_form=pitch_form,pitches=pitches,comments=comments,upvotes=upvotes,downvotes=downvotes,user_votes=user_votes)



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
  comments_count=get_all_comments([pitch])
  upvotes=get_all_upvotes([pitch])
  downvotes=get_all_downvotes([pitch])
  if current_user.is_authenticated:
    user_votes=get_user_votes([pitch])
  else:
    user_votes=None
  return render_template('pitch.html',pitch=pitch,comment_form=comment_form,comments=comments_list,comments_count=comments_count,downvotes=downvotes,upvotes=upvotes,user_votes=user_votes)

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
  user_votes=get_user_votes(my_pitches)
  return render_template('profile/profile.html',pitches=my_pitches,user=current_user,comments=comments,upvotes=upvotes,downvotes=downvotes,user_votes=user_votes)
  # return render_template('profile/profile.html',user=current_user,pitches=my_pitches)


@main.route('/category/<category_name>')
def category(category_name):
  category_pitches=Pitch.query.filter_by(category=Category.query.filter_by(name=category_name).first()).order_by(Pitch.id.desc()).all()
  comments=get_all_comments(category_pitches)
  upvotes=get_all_upvotes(category_pitches)
  downvotes=get_all_downvotes(category_pitches)
  if(current_user.is_authenticated):
    user_votes=get_user_votes(category_pitches)
  else:
    user_votes=None
  return render_template('index.html',pitches=category_pitches,comments=comments,upvotes=upvotes,downvotes=downvotes,category=category_name,user_votes=user_votes)


@main.route('/pitch/<pitch_id>/<action>')
@login_required
def vote(pitch_id,action):
  #check for existing vote
  target_pitch=Pitch.query.filter_by(id=pitch_id).first()
  # existing_vote=None
  existing_vote=Vote.query.filter_by(user=current_user,pitch=target_pitch).first()

  if existing_vote:
    if action=='upvote':
      existing_vote.upvote=not existing_vote.upvote
      existing_vote.downvote=False
      existing_vote.save_vote()
    elif action=='downvote':
      existing_vote.downvote=not existing_vote.downvote
      existing_vote.upvote=False
      existing_vote.save_vote()
  else:
    if action=='upvote':
      new_vote=Vote(upvote=True,user=current_user,pitch=target_pitch)
      new_vote.save_vote()

    elif action=='downvote':
      new_vote=Vote(downvote=True,user=current_user,pitch=target_pitch)
      new_vote.save_vote()
  flash('Vote updated','success')
  return redirect(request.referrer)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@main.route('/user/<username>/profile/update',methods=['GET','POST'])
@login_required
def update_profile(username):
  user=User.query.filter_by(username=current_user.username).first()
  if request.method=='POST':
    
    photo=request.files['photo']
    if photo and allowed_file(photo.filename):
      bio=request.form.get('bio')
      filename=secure_filename(photo.filename)
      photo.save(os.path.join('app/static/photos',filename))
      user.profile_pic_path=f'photos/{filename}'
      if bio:
        user.bio=bio
        user.save_user()
      user.save_user()
      flash('Update Successful','success')
    else:
      flash('Please provide a valid file','error')

  return render_template('profile/update.html',user=current_user)
