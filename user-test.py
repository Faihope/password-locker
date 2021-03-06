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
        
    def test_init(self):
        
        '''
        test case to test if the object is initialized properly
        '''
        
        self.assertTrue(self.new_user.username,'faith')
        self.assertTrue(self.new_user,'password')
        
    def test_save_accounts(self):
        '''
        to test if the account is saved
        '''
        self.new_user.save_account()
        self.assertEqual(len(User.user_list),1)
        
    def tearDown(self):
        '''
        it cleans up after each testcase has run
        '''
        User.user_list = []
        
    def test_display_account(self):
        '''
        returns the list of all saved accounts
        '''
        self.assertEqual(User.display_account(),User.user_list)    
    
    def test_delete_account(self):
         '''
         to test if we can remove contact from our list
         '''
         self.new_user.save_account()
         test_user = User('test','1234')#new account
         test_user.save_account()
         
         self.new_user.delete_account()
         self.assertEqual(len(User.user_list),1)   

if __name__ == '__main__':
    unittest.main()    
        
    
        
        
        
        
    

    
    
    
