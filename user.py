class User:
    '''
    class that generates new instace of user
    '''
    
    user_list = []
    
    def __init__(self,username,password):
        self.username = username
        self.password = password
        
    def save_user(self):
        '''
        save_user method saves a new user objects to the user list
        '''
        User.user_list.append(self)
        
      
       
    