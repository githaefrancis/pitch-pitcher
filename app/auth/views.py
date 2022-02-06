from flask import render_template
from . import auth
from .forms import RegistrationForm,LoginForm

@auth.route('/login')
def login():
  return '<h1>Login page</h1>'

@auth.route('/register')
def register():
  register_form=RegistrationForm()
  return render_template('auth/register.html',register_form=register_form)