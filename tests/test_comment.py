import unittest
from app.models import User,Comment,Pitch,Category,Role

class CommentModelTest(unittest.TestCase):
  def setUp(self):
    self.new_user=User(name="Francis",password='password',role=Role.query.filter_by(name='User').first())
    self.new_pitch=Pitch(category=Category.query.filter_by(name='interview').first(),user=self.new_user)
    self.new_comment=Comment(user=self.new_user,pitch=self.new_pitch,content='Good stuff')


  def tearDown(self):
    Comment.query.delete()
    Pitch.query.delete()
    User.query.delete()

  def test_check_instance_variables(self):
    self.assertEquals(self.new_comment.user,self.new_user)
    self.assertEquals(self.new_comment.pitch,self.new_pitch)
    self.assertEquals(self.new_comment.content,'Good stuff')

  def test_save_comment(self):
    self.new_comment.save_comment()
    self.assertTrue(len(Comment.query.all())==1)

