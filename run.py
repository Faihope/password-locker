import random
from user import User

#create a contact
def create_accounts(username,password):
    '''
    Function to create new account
    '''
    new_account = User(username,password)
    return new_account

   #save contacts
def save_accounts(account):
    '''
    method to save the user account
    '''
    account.save_account()
    
def del_account(account):
    '''
    funcion to delete account
    '''
    account.delete_contact()
    
    

def main():
    print("Hello welcome to Your password locker.What is your name?")
    username = input()
    
    print(f"Hello {username}. What would you like to do?")
    print('\n')
  
    
        
        
main()        
