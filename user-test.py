import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the contact class behaviours
    Args:
         unnitest.Testcase:Testcase class that helps in creating test cases
    '''
    
    def setUp(self):
        '''
        Set up method to run before a test case
        '''
        
        self.new_user = User('faith','1234')
        
    def test_save_user(self):
        
        '''
        test case to test if the object is initialized properly
        '''
        
        self.assertEqual(self.new_user.username,'faith')
        self.assertEqual(self.new_user,'password')
        
        
        
        
    

    
    
    
