import unittest
from CredentialsData import CredentialsData

class TestCredentials(unittest.TestCase):
    def setUp(self):
        """
        setUp method
        """
        self.new_credential = CredentialsData("Gmail", "cliff", "lolololo")
        
    def test_init(self):
        """
        testing initialization
        """
        self.assertEqual(self.new_credential.platform, "Gmail")
        self.assertEqual(self.new_credential.username, "cliff")
        self.assertEqual(self.new_credential.password, "lolololo")    
