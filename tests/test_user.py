from ast import Not
import unittest
from app.models import User,Role

class UserModelTest(unittest.TestCase):
  def setUp(self):
    self.new_user=User(name="Francis",password='password',role=Role.query.filter_by(name='User').first())

  def tearDown(self):
    User.query.delete()
    

  def test_password_setter(self):
    self.assertTrue(self.new_user.password_secure is not None)
  
  def test_no_access_password(self):
    with self.assertRaises(AttributeError):
      self.new_user.password

  def test_password_verification(self):
    self.assertTrue(self.new_user.verify_password('password'))

  def test_save_user(self):
    self.new_user.save_user()
    self.assertTrue(len(User.query.all())==1)

  