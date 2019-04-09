import random

class User:
    '''
    class that creates instances of user
    '''

    user_details = []

    def save_user(self):
        User.user_details.append(self)

    def __init__(self first_name, last_name, login_name):
        self.first_name =first_name
        self.last_name = last_name
        self.login_name = login_name

class Credentials:
    '''
    class that creates instances of credentials
    '''

    credentials_list = []

    def save_credentials(self):
        Credentials.credentials_list.append(self)

    def __init__(self app_name, user_name, password):
        self.app_name = app_name
        self.user_name = user_name
        self.password = password



    def password_gen():
        return random.randint(11, 99) + str(random.randint(111, 499) + random.randint(33, 77) 

   

