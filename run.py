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
    
# def delete_account(account):
#     '''
#     funcion to delete account
#     '''
#     account.delete_account(account)
    
def display_account():
    '''
    returns all saved accounts
    '''
    return User.display_account()
    
    

def main():
    print("Hi there, welcome to Your password locker.What is your name?")
    username = input()
    
    print(f"Hello {username}. What would you like to do?")
    print('\n')
    
    while True:
        print("Use these short codes: ca - create a new account,da - display account,lg - login to account, ex - exit password locker,del - delete account")
        short_code = input().lower()
        # print('\n')
        
        if short_code == 'ca':
            print("Create Your Username")
            username =input()
            
            print("Create password")
            password = input()
            # print("New account")
            
            print('Confirm password')
            confirm_password =input()
            
            while confirm_password !=password:
                print("Passwords did not match")
                print("Enter your password")
                password = input()
                print("confirm password")
                confirm_password = input()
                
            else:
                print(f"Congratulations {username} your account has been created successfully")
                print("\n")
            
            save_accounts(create_accounts(username,password))
            print('\n')
            print(f"new Account {username}  with password {password} created")
            print('\n')
            
       
            print("Welcome,Proceed to login")
            print("username")
            entered_username = input()
            
            print("Your password")
            entered_password = input()
            
            while entered_username != username or entered_password != password:
                  print("Invalid username or password")
                  print("username")
                  username = input()
                  
                  print("password")
                  password = input()
            else:
                print("\n")
                print("login successfull")
                
        elif short_code =='lg':
            print("Welcome")
            print("Enter username")
            default_username = input()
            print("Enter password")
            default_password = input()
            print("\n")
            
            while default_username != 'newuser' or default_password != '12345':
                print("Wrong username or password use username newuser and password 12345 to login")
                print("\n")
                
                print("Enter Username")
                default_username =input()
                
                print("Enter password")
                default_password = input()
                
            else:
                print('Login success')
            
        elif short_code == 'da':
            if display_account():
                print("Here is a list of all your accounts and passwords")
                print('\n')
                
                for account in save_accounts():
                    print(f"{account.username} {account.password}")
                    print('\n')
                    
            else:
                print('\n')
                print("You dont seem to have any account saved yet")
                print('\n')
        elif short_code == 'del':
            print('Enter the username to delete')
            username = input()
            
            User.delete_account(username)
            print(f"Your account {username} has been deleted successfully") 
               
                
        elif short_code == 'ex':
            print("Thank you for choosing password locker....byeee")
            break
        else:print("I really didnt get that.Please use the short codes")
            
    
        
if __name__=='__main__':
    main()      
