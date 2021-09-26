import unittest 
from app.models import Comments
 
class CommentsTest(unittest.TestCase): 
  
  def setUp(self):
    self.new_comment = Comments(comment="Love your site",user_id = 1,blog_id=1 )
  
  def test_instance(self): 
    self.assertTrue(isinstance(self.new_comment,Comments))
    
  def test_check_instance_variables(self):
    self.assertEquals(self.new_comment.comment,"Love your site")
    self.assertEquals(self.new_comment.user_id,1)
    self.assertEquals(self.new_comment.blog_id,1)
    
  def test_save_comment(self):
    self.new_comment.save_comment()
    self.assertTrue(len(Comments.query.all())>0)
    
  def test_get_comment(self):
    found_comment=self.new_comment.get_comments(1)
    self.assertTrue(found_comment is not None)
