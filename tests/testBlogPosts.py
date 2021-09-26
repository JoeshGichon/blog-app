import unittest 
from app.models import BlogPosts
 
class BlogsTest(unittest.TestCase): 
  
  def setUp(self):
    self.new_blog = BlogPosts(title="Favourite pet",blog="My favourite pet is a cat",user_id = 1 )
  
  def test_instance(self): 
    self.assertTrue(isinstance(self.new_blogpost,BlogPosts))
    
  def test_check_instance_variables(self):
    self.assertEquals(self.new_blogpost.title,"Favourite Pet")
    self.assertEquals(self.new_blogpost.content,"My favourite pet is a cat")
    self.assertEquals(self.new_blogpost.user_id,1)
    
  def test_save_blog(self):
    self.new_blog.save_blogpost()
    self.assertTrue(len(BlogPosts.query.all())>0)
