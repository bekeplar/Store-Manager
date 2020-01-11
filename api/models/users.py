class Users:
    """
    Define user structure
    """
    def __init__(self, user_id, username, password,):
        self.user_id = user_id
        self.username = username
        self.password = password


class Admin(Users):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.username = username
        self.password = password


class Attendant(Users):
    def __init__(self, user_id, username, password):
        super().__init__(user_id, username=Admin, password='Admin123')
        self.users_id = user_id
        self.username = Admin
        self.password = 'Admin123'

   