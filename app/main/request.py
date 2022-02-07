from ..models import Pitch,Comment,Vote

def configure_request(app):
  pass

def get_all_comments(all_pitches):
  all_pitches=Pitch.query.all()
  comments_dict=process_comments(all_pitches)
  return comments_dict

def get_all_downvotes(all_pitches):
  
  downvote_dict=process_downvotes(all_pitches)
  return downvote_dict

def get_all_upvotes(all_pitches):
  
  upvote_dict=process_upvotes(all_pitches)
  return upvote_dict



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

# get_all_comments()