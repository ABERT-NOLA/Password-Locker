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