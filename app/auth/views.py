from flask import render_template,redirect,url_for,flash,request
from . import auth
from .forms import RegistrationForm,LoginForm
from .. import db
from flask_login import login_user,logout_user,login_required
from ..models import User,Role
from ..email import mail_message

@auth.route('/login',methods=['GET','POST'])
def login():
  login_form=LoginForm()
  if login_form.validate_on_submit():
    user=User.query.filter_by(email=login_form.email.data).first()
    if user is not None and user.verify_password(login_form.password.data):
      login_user(user,login_form.remember)
      return redirect(request.args.get('next') or url_for('main.index'))
    flash('Invalid username or password')
  title="Pitch Pitcher Login"
  return render_template('auth/login.html',login_form=login_form)

@auth.route('/register',methods=["GET","POST"])
def register():
  register_form=RegistrationForm()
  if register_form.validate_on_submit():
    user=User(name=register_form.name.data,email=register_form.email.data,username=register_form.username.data,password=register_form.password.data,role=Role.query.filter_by(name='User').first())
    user.save_user()

    mail_message("Welcome to Pitch Pitcher","email/welcome_user",user.email,user=user)
    return redirect(url_for('auth.login'))
  return render_template('auth/register.html',register_form=register_form)


@auth.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for("main.index"))

