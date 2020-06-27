#!/usr/bin/env python3.6

import random
import string

from UserData import UserData
from CredentialsData import CredentialsData

def new_users(name_one, name_two, email_address, user_name, pass_word):

    """
    creates new user 
    """
    new_user = UserData(name_one, name_two, email_address, user_name, pass_word)
    
    return new_user
    
def save_accounts(account):
    """
    save new user account
    """
    account.save_account()

def check_user(used_name, used_password):
    """
    checks if user exists
    """
    user_exists = UserData.user_login(used_name, used_password)

    return user_exists    
