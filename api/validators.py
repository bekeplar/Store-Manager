import re


class Validators:
    """validates product and return appropriate message"""

    def product_validation(
        self,
        product_name,
        product_id,
        product_quantity,
        product_price
                ):

        if not product_name:
            return "product_name is missing"
        if product_name == " ":
            return "product_name is missing"
        if not re.match(r"^([a-zA-Z]+\s)*[a-zA-Z]+$", product_name):
            return "product_name must have no white spaces"
        if not re.match(r"^[0-9]*$", product_quantity):
            return "quantity must be only digits and must have no white spaces"
        if not re.match(r"^[0-9]*$", product_price):
            return "price must be only digits and must have no white spaces"
        if len(product_name) < 2:
            return "product_name should be more than 2 characters long"
        if not product_quantity:
            return "quantity is missing"
        if product_quantity == " ":
            return "quantity is missing"
        if product_quantity < 1:
            return "quantity should be at least 1 item"
        if not product_price:
            return "price is missing"
        if product_price < 1:
            return "price should be greater than zero"
        if product_price == " ":
            return "price is missing"

    def validate_input_type(self, input):
        try:
            _input = int(input)
        except ValueError:
            return "Input should be an interger"

    def validate_product_quantity(self, product_quantity):
        if not re.match(r"^[0-9]*$", product_quantity):
            return "quantity must be only digits and must have no white spaces"
        if not product_quantity:
            return "quantity is missing"
        if product_quantity == " ":
            return "quantity is missing"
        if int(product_quantity) < 1:
            return "quantity should be at least 1 item"

    def sales_validation(
        self,
        product_name,
        sale_id,
        product_quantity,
        product_price
                ):

        if not product_name:
            return "product_name is missing"
        if product_name == " ":
            return "product_name is missing"
        if not re.match(r"^([a-zA-Z]+\s)*[a-zA-Z]+$", product_name):
            return "product_name must not be empty"
        if not re.match(r"^[0-9]*$", product_quantity):
            return "quantity must be a number"
        if not re.match(r"^[0-9]*$", product_price):
            return "price must be only digits "
        if len(product_name) < 2:
            return "product_name should be more than 2 characters"
        if not product_quantity:
            return "quantity is missing"
        if product_quantity == " ":
            return "quantity is missing"
        if product_quantity < 1:
            return "quantity should be at least 1 item"
        if not product_price:
            return "price is missing"
        if product_price < 1:
            return "price should be greater than zero"
        if product_price == " ":
            return "price is missing"
