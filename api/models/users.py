class User:
    """
    Define user structure
    """
    def __init__(self, user_id, username, password, is_admin):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.is_admin = is_admin
