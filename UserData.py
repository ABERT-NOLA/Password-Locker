class UserData:
    """
    Class that generates new user accounts.
    """

    create_account = [] # Empty user list

    def __init__(self,first_name,last_name,email,user_name,pass_word):

      # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.email=email
        self.user_name=user_name
        self.pass_word=pass_word

    def save_account(self):

        """
        saves the new user to create_account list
        """

        UserData.create_account.append(self)
        
    @classmethod
    def user_login(cls, used_name, used_password):
        """
        checks whether user exists
        """
        for user in UserData.create_account:
            if user.username == used_name and user.password == used_password:
                return user
            return False