import os


class Config:
  '''
  General configuration parent class
  '''

  pass

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
  DEBUG=True

class TestConfig(Config):
  '''
  Production configuration child class

  Args:
      Config: The configutation for test environment
  '''
  pass

config_options={
  'development':DevConfig,
  'production':ProdConfig,
  'test':TestConfig
}