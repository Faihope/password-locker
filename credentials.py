from user import User


class Credentials:
    '''
    A class to create instance of credentials
    '''
    
    user_credentials = []
    
def __init__(self,save_username,save_password):
    self.save_username = save_username
    self.save_password = save_password
    
    
def save_credentials(self):
    '''
    saves new credentials of the user
    '''
    
    User.user_credentials.append(self)