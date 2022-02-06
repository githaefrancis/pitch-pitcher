from flask import render_template,redirect,url_for,flash,request
from . import auth
from .forms import RegistrationForm,LoginForm
from .. import db
from flask_login import login_user,logout_user,login_required
from ..models import User,Role
@auth.route('/login')
def login():
  login_form=LoginForm()
  return render_template('auth/login.html',login_form=login_form)

@auth.route('/register',methods=["GET","POST"])
def register():
  register_form=RegistrationForm()
  if register_form.validate_on_submit():
    user=User(name=register_form.name.data,email=register_form.email.data,username=register_form.username.data,password=register_form.password.data,role=Role.query.filter_by(name='User').first())
    user.save_user()
    return redirect(url_for('auth.login'))
  return render_template('auth/register.html',register_form=register_form)