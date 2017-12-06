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

    def tearDown(self):
        '''
         tear down method that does clean up after each test case has run.
        '''
        User.user_list = []


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

    def test_save_multiple_user(self):

        '''
        tests if we can save multiple users to the user list
        '''

        self.new_user.save_user()
        test_user = User("user","root") 
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)
        

    def test_delete_user(self):

        '''
        test delete user to test if we can removea contact from our list
        '''

        self.new_user.save_user()
        test_user = User("user", "root")
        test_user.save_user()
        self.new_user.delete_user() #to delete a user object
        self.assertEqual(len(User.user_list),1)


    def test_find_user_by_username(self):

        '''
        test to check if we can find a user by the user name and display information
        '''

        self.new_user.save_user()
        test_user = User("ralph","root")
        test_user.save_user()
        found_user = User.find_by_username("ralph")
        self.assertEqual(found_user.email,test_user.password)
        



if __name__ == '__main__':
    unittest.main()