from ..models import Pitch,Comment,Vote
from flask_login import current_user


def configure_request(app):
  pass

def get_all_comments(all_pitches):
  # all_pitches=Pitch.query.all()
  comments_dict=process_comments(all_pitches)
  return comments_dict

def get_all_downvotes(all_pitches):
  
  downvote_dict=process_downvotes(all_pitches)
  return downvote_dict

def get_all_upvotes(all_pitches):
  
  upvote_dict=process_upvotes(all_pitches)
  return upvote_dict

def get_user_votes(all_pitches):
  user_votes=process_user_votes(all_pitches)
  return user_votes

def process_comments(pitch_list):
  comment_dict={}
  for pitch in pitch_list:
    comment_count=Comment.query.filter_by(pitch=pitch).count()
    comment_dict[pitch.id]=comment_count
  return comment_dict

def process_downvotes(pitch_list):
  downvote_dict={}
  for pitch in pitch_list:
    downvote_count=Vote.query.filter_by(pitch=pitch,downvote=True).count()
    downvote_dict[pitch.id]=downvote_count

  return downvote_dict

def process_upvotes(pitch_list):
  upvote_dict={}
  for pitch in pitch_list:
    upvote_count=Vote.query.filter_by(pitch=pitch,upvote=True).count()
    upvote_dict[pitch.id]=upvote_count

  return upvote_dict


def process_user_votes(pitch_list):
  user_votes_dict={}
  for pitch in pitch_list:
    downvote_exist=Vote.query.filter_by(pitch=pitch,downvote=True,user=current_user).first()
    upvote_exist=Vote.query.filter_by(pitch=pitch,upvote=True,user=current_user).first()

    if downvote_exist:
      user_votes_dict[pitch.id]='downvote'
    
    elif upvote_exist:
      user_votes_dict[pitch.id]='upvote'

    else:
      user_votes_dict[pitch.id]=None
  print(user_votes_dict)
  return user_votes_dict


# get_all_comments()