import random
from user import User
from credentials import Credentials

# functions to add our credentials

def create_new_credential(account_name,account_password):
    new_credential = Credentials(account_name,account_password)

    return new_credential

def save_new_credential(credentials):

    credentials.save_credentials()

def find_credential(account_name):

    return Credentials.find_by_name(account_name)

def display_credential():

    return Credentials.display_credentials()  

def delete_credential(credentials):

    return Credentials.delete_credentials(credentials)
