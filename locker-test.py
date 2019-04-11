from locker import Credentials
from locker import User
import unittest
import pyperclip

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines the test cases for creating and authenticating credentials
    '''
    def setUp(self):
        
        self.new_user = Credentials(1,"john","doe")
    
    def tearDown(self):
        '''
        Clean up after each test has run
        '''
        Credentials.users_list = []
    
    def test_init(self):
        '''
        Test case to test if the case has been initialized properly
        '''
        self.assertEqual(self.new_user.auth,1)
        self.assertEqual(self.new_user.user_name,"john")
        self.assertEqual(self.new_user.password,"doe")
    
    def test_create(self):
        '''
        Testing if the new credential is saved into the list
        '''
        self.new_user.create_account()
        self.assertEqual(len(Credentials.users_list),1)
    
    def test_authenticate(self):
        '''
        Test to check if the authenticate function can sign in a user properly
        '''
        self.new_user.create_account()
        test_account = Credentials(1,"Test","Password")
        test_account.create_account()

        found_user = Credentials.auth_user("Test","Password")
        self.assertEqual(found_user.auth_user , test_account.auth_user)

class TestUserData(unittest.TestCase):
    '''
    Test class that defines the test cases for creating websites log in credentials
    '''
    def setUp(self):
        '''
        Setting up the structure before each test
        '''
        self.new_data = User(1,1,"facebook.com","poiii")
    
    def tearDown(self):
        '''
        Clean up the test after test is complete
        '''
        User.data_list = []
    
    def test_init(self):
        '''
        Test case to evaluate if the case has been initialized properly
        '''
        self.assertEqual(self.new_data.identify,1)
        self.assertEqual(self.new_data.data_id,1)
        self.assertEqual(self.new_data.app_name,"facebook.com")
        self.assertEqual(self.new_data.app_key,"poiii")

    def test_add_password(self):
        '''
        Test if the new app and password can be saved
        '''
        self.new_data.add_password()
        self.assertEqual(len(User.data_list),1)

    def test_display_data(self):
        '''
        Test if data can be displayed.
        '''
        self.new_data.add_password()
        test_data = User(1,1,"facebook.com","poiii")
        test_data.add_password()

        data_found = User.display_data(1,1)
        self.assertEqual(data_found.app_name,test_data.app_name)
    
    def test_data_exists(self):
        '''
        Test to check if the function for checking data works 
        '''
        self.new_data.add_password()
        test_data = User(1,1,"facebook.com","tpgh")
        test_data.add_password()

        data_exists = User.existing_data(1)
        self.assertTrue(data_exists)
    
    def test_copy_password(self):
        '''
        Test if the copy password function works
        '''
        self.new_data.add_password()
        User.copy_password(1,1)

        self.assertEqual(self.new_data.app_key,pyperclip.paste())


if __name__ == "__main__":
    unittest.main()