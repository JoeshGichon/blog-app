import unittest
from app.models import Quotes 

class QuotesTest(unittest.TestCase): 
  def setUp(self):
    self.new_quote = Quotes("John Doo","Be your own boss")
    
  def test_init(self): 
    self.assertEqual(self.new_quote.author,"John Doo")
    self.assertEqual(self.new_quote.quote,"Be your own boss")
