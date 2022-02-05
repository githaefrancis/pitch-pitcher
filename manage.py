from app import create_app,db
from app.models import User,Comment,Pitch,Category,Role
from flask_migrate import Migrate





app=create_app('development')
migrate=Migrate()
migrate.init_app(app,db)

@app.shell_context_processor
def make_shell_context():
  return dict(app=app,db=db,User=User,Comment=Comment,Pitch=Pitch,Category=Category,Role=Role)

if __name__=='__main__':
  app.run()