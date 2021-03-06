import unittest 
from user import User


class TestUser(unittest.TestCase):


    '''
    Test class that defines test cases for the User class behaviors


    Args:
        unittest.TestCase :Test case that helps in creating test cases

    '''

    def setUp(self):

        '''
        method to run before each test case
        '''

        self.new_user = User("seth","password")


    def test_init_(self):

        '''
        test case to if the User object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name,"seth")
        self.assertEqual(self.new_user.password,"password")

    def test_save_user(self):

        '''
        test case to test if user objects have been saved into user_list
        '''

        self.new_user.save_user() #save new user
        self.assertEqual(len(User.user_list),1)


   
if __name__ == '__main__':
    unittest.main()