from . import main


@main.route('/')
def index():
  return '<h1>Home</h1>'