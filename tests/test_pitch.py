import unittest
from app import db
from app.models import Category, Pitch, User,Role

class PitchModelTest(unittest.TestCase):
  def setUp(self):
    self.new_user=User(name="Francis",password='password',role=Role.query.filter_by(name='User').first())
    self.new_pitch=Pitch(category=Category.query.filter_by(name='interview').first(),user=self.new_user)

  def tearDown(self):
    Pitch.query.delete()
    User.query.delete()
    

  def test_check_instance_variables(self):

    self.assertEquals(self.new_pitch.user,self.new_user)
    self.assertEquals(self.new_pitch.category,Category.query.filter_by(name='interview').first())

  def test_save_pitch(self):
    self.new_user.save_user()
    self.new_pitch.save_pitch()
    self.assertTrue(len(Pitch.query.all())==1)
