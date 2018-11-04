from api.models.validation import empty_field


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


class ValidateUserInput:

    def validate_input_data(self, request_data):
        """
        Validates input data from the new user form
        Args:
            request_data(object): request Object that holds form data
        Retruns:
            dict: {"errors", True} for no errors {"", False} if errors present
        """
        errors = {}
        if not request_data["username"].strip():
            errors.update({"username": "Username is required"})

        if not request_data["password2"]:
            errors.update({"password2": "Confirm password is required"})

        if request_data["password"] != request_data["password2"]:
            errors.update({"password": "Passwords do not match"})

        if not request_data["roles"]:
            errors.update({"roles": "User role is required"})

        return {
            "errors": errors,
            "is_true": empty_field(self, errors)
        }

    def validate_login_input(self, request_data):
        """
        Validates input data from the login form
        Args:
            request_data(object): request Object that holds form data
        Retruns:
            dict: {"errors", True} for no errors {"", False} if errors present
        """
        errors = {}
        if not request_data["username"]:
            errors.update({"username": "Username is required"})

        if not request_data["password"]:
            errors.update({"password": "Password is required"})

        return {
            "errors": errors,
            "is_true": empty_field(self, errors)
        }   