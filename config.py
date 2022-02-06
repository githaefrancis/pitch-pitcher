import os


class Config:
  '''
  General configuration parent class
  '''

  SECRET_KEY=os.environ.get("SECRET_KEY")
  SIMPLEMDE_JS_IIFE=True
  SIMPLEMDE_USE_CDN=True


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