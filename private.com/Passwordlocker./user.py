import unittest
from credentials import Credentials # impoting the credentials class 

class User:
    """
    Class that generates new instances of user accounts 
    """

    # start 
    user_list = [] # Empty user list 
    def __init__(self,user_name,user_password):

        '''
        __init__ method to define the properties of a User object

        Args:
            user_name : the name of the user 
            user_password : the user's password
        '''

        self.user_name = user_name
        self.user_password = user_password

    def save_user(self):
        """
        saving a user to the user list
        """
        User.user_list.append(self)
