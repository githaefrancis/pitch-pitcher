import unittest
from app.models import User, Comment,Category,Vote,Pitch,Role

class VoteModelTest(unittest.TestCase):
  def setUp(self):
    self.new_user=User(name="Francis",password='password',role=Role.query.filter_by(name='User').first())
    self.new_pitch=Pitch(category=Category.query.filter_by(name='interview').first(),user=self.new_user)
    self.new_vote=Vote(user=self.new_user,pitch=self.new_pitch,upvote=True)

  def tearDown(self):
    Vote.query.delete()
    Pitch.query.delete()
    User.query.delete()

  def test_instance_variables(self):
    self.assertEquals(self.new_vote.user,self.new_user)
    self.assertEquals(self.new_vote.pitch,self.new_pitch)
    self.assertEquals(self.new_vote.upvote,True)