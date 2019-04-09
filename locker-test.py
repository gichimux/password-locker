import unittest
from locker import User
from locker import Credentials

class TestUser(unittest.TestCase):
    '''
    test case that defines tests for user class
    '''
    def setUp(self):
        self.new_user= User("john", "doe", "jd")

if name = '__main__':
    unittest.main()