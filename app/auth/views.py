from flask import render_template
from . import auth
from .forms import RegistrationForm,LoginForm

@auth.route('/login')
def login():
  login_form=LoginForm()
  return render_template('auth/login.html',login_form=login_form)

@auth.route('/register')
def register():
  register_form=RegistrationForm()
  return render_template('auth/register.html',register_form=register_form)