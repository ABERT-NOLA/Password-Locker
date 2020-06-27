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