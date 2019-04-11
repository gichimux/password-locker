import random

class User:
    '''
    class that creates instances of user
    '''

    user_details = []

    def save_user(self):
        User.user_details.append(self)

    def __init__(self, first_name, last_name, login_name):
        self.first_name =first_name
        self.last_name = last_name
        self.login_name = login_name

class Credentials:
    '''
    class that creates instances of credentials
    '''
    #create a dictionary to save credentials as {'app_name': 'user_name, password'}
    def create_credentials_dict():
        credentials_dict = {}
        store_passwords(app_name, password, user_name)

    #store credentials in the dictionary
    def store_credentials(cls, credentials_dict ):
        credentials_dict[app_name] = password + user_name 


    def __init__(self, app_name, user_name, password):
        self.app_name = app_name
        self.user_name = user_name
        self.password = password


    #method to generate passwords for user
    def password_gen():
        return random.randint(11, 99) + str(random.randint(111, 499) + random.randint(33, 77) 

    
    
  
        
  

   

