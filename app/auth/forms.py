from ast import Pass
import email
from . import views,forms

from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import InputRequired,Email,EqualTo

from wtforms import ValidationError
from ..models import User


class RegistrationForm(FlaskForm):
  email=StringField('Your Email Address',validators=[InputRequired(),Email()])
  name=StringField('Your Name',validators=[InputRequired()])
  username=StringField('Your username',validators=[InputRequired()])
  password=PasswordField('Password',validators=[InputRequired(),EqualTo('password_confirm',message='Password must match')])
  password_confirm=PasswordField('Confirm Password',validators=[InputRequired()])
  submit=SubmitField('Sign Up')

  def validate_email(self,data_field):
    if User.query.filter_by(email=data_field.data).first():
      raise ValidationError('There is an account with that email')

  def validate_username(self,data_field):
    if User.query.filter_by(email=data_field.data).first():
      raise ValidationError('That username is taken')

class LoginForm(FlaskForm):
  email=StringField('Your Email Address',validators=[InputRequired(),Email()])
  password=PasswordField('Password',validators=[InputRequired()])
  remember=BooleanField('Remember me')
  submit=SubmitField('Sign In')     