class User:

    '''
    class that generates new instance of user
    '''

    user_list = []

    def __init__(self,user_name,password,number):
        self.user_name = user_name
        self.password = password
        self.number = number
        

    def save_user(self):

        '''
        save_user method saves a new user objects to the user_list
        '''

        User.user_list.append(self)


    def delete_user(self):

        '''
        delete user method deletes a saved user from user list
        '''

        User.user_list.remove(self)


    @classmethod
    def find_by_username(cls,number):

        '''
        method that takes in a number and returns a user that matches that number
        
        Args:
            number:phone number to search for
        Returns:
        user that matches that number
        '''

        for user in cls.user_list:
            if user.phone_number == number:
                return user
