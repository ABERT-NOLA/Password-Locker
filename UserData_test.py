import unittest # Importing the unittest module
from UserData import UserData # Importing the contact class

class TestuserData(unittest.TestCase):
    def setUp(self):
        """
        set up method
        """
        self.new_user = UserData("cliff", "kasera", "ckasera@gmail.com", "Blankphrase", "lololo") 

    
