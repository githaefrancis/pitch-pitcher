
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class User(UserMixin,db.Model):
  '''
  User class that defines user objects
  '''
  __tablename__='users'
  id=db.Column(db.Integer,primary_key=True)
  name=db.Column(db.String(255))
  email=db.Column(db.String(255),unique=True,index=True)
  username=db.Column(db.String(255))
  bio=db.Column(db.String(255))
  profile_pic_path=db.Column(db.String(255))
  password_secure=db.Column(db.String(255))
  role_id=db.Column(db.Integer,db.ForeignKey("roles.id"))
  Pitches=db.relationship('Pitch',backref='user', lazy='dynamic')
  Votes=db.relationship('Vote',backref='user',lazy='dynamic') 
  Comments=db.relationship('Comment',backref='user',lazy='dynamic') 
  @property
  def password(self):
    raise AttributeError('You cannot read the password attribute')

  @password.setter
  def password(self,password):
    self.password_secure=generate_password_hash(password)

  def verify_password(self,password):
    return check_password_hash(self.password_secure,password)

  def save_user(self):
    db.session.add(self)
    db.session.commit()

  def __repr__(self):
    return f'User {self.username}'

class Role(db.Model):
  __tablename__='roles'
  id=db.Column(db.Integer,primary_key=True)
  name=db.Column(db.String(255))
  users=db.relationship('User',backref='role', lazy='dynamic')

  def __repr__(self):
    return f'User {self.name}'

class Pitch(db.Model):
  __tablename__="pitches"
  id=db.Column(db.Integer,primary_key=True)
  user_id=db.Column(db.Integer,db.ForeignKey("users.id"))
  Comments=db.relationship('Comment',backref='pitch', lazy='dynamic')
  category_id=db.Column(db.Integer,db.ForeignKey("categories.id"))
  Votes=db.relationship('Vote',backref='pitch',lazy='dynamic')
  pitch_date=db.Column(db.DateTime,default=datetime.utcnow)

  def save_pitch(self):
    db.session.add(self)
    db.session.commit()

class Comment(db.Model):
  __tablename__='comments'
  id=db.Column(db.Integer,primary_key=True)
  pitch_id=db.Column(db.Integer,db.ForeignKey("pitches.id"))
  time_posted=db.Column(db.DateTime,default=datetime.utcnow)
  content=db.Column(db.String(255))
  user_id=db.Column(db.Integer,db.ForeignKey("users.id"))

  def save_comment(self):
    db.session.add(self)
    db.session.commit()
class Category(db.Model):
  __tablename__='categories'
  id=db.Column(db.Integer,primary_key=True)
  name=db.Column(db.String(255))
  Pitches=db.relationship('Pitch',backref='category',lazy='dynamic')

  
class Vote(db.Model):
  __tablename__='votes'
  id=db.Column(db.Integer,primary_key=True)
  voted_on=db.Column(db.DateTime,default=datetime.utcnow)
  downvote=db.Column(db.Boolean,default=False)
  upvote=db.Column(db.Boolean,default=False)
  user_id=db.Column(db.Integer,db.ForeignKey("users.id"))
  pitch_id=db.Column(db.Integer,db.ForeignKey("pitches.id"))  


  def save_vote(self):
    db.session.add(self)
    db.session.commit()