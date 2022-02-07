import os


class Config:
  '''
  General configuration parent class
  '''

  SECRET_KEY=os.environ.get("SECRET_KEY")
  SIMPLEMDE_JS_IIFE=True
  SIMPLEMDE_USE_CDN=True

  MAIL_SERVER='smtp.googlemail.com'
  MAIL_PORT=587
  MAIL_USE_TLS=True
  MAIL_USERNAME=os.environ.get("MAIL_USERNAME")
  MAIL_PASSWORD=os.environ.get("MAIL_PASSWORD")
  

class ProdConfig(Config):
  '''
  Production configuration child class

  Args:
      Config: The configutation for production environment
  '''
  pass

class DevConfig(Config):
  '''
  Production configuration child class

  Args:
      Config: The configutation for dev environment
  '''
  SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:1234@localhost/pitch_pitcher'
  DEBUG=True

class TestConfig(Config):
  '''
  Production configuration child class

  Args:
      Config: The configutation for test environment
  '''
  SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:1234@localhost/pitch_pitcher_test'
  

config_options={
  'development':DevConfig,
  'production':ProdConfig,
  'test':TestConfig
}