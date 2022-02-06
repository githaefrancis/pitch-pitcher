from . import auth


@auth.route('/login')
def login():
  return '<h1>Login page</h1>'