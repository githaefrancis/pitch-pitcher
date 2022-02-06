import unittest
from app import db
from app.models import Category, Pitch, User,Role

class PitchModelTest(unittest.TestCase):
  def setUp(self):
    self.new_user=User(name="Francis",password='password',role=Role.query.filter_by(name='User').first())
    self.new_pitch=Pitch(downvotes=0,upvotes=0,category=Category.query.filter_by(name='inteview').first(),user=self.new_user)

  def test_check_instance_variables(self):
    self.assertEquals(self.new_pitch.downvotes,0)
    self.assertEquals(self.new_pitch.upvotes,0)
    self.assertEquals(self.new_pitch.user,self.new_user)
    self.assertEquals(self.new_pitch.category_id,4)