import datetime
import uuid
from flask import jsonify
from api.models.validation import empty_field


class Products:
    """This class defines the products sold by the store"""

    def __init__(self, product_name,  product_price, product_quantity):
        self.product_id = uuid.uuid4()
        self.product_quantity = product_quantity
        self.product_price = product_price
        self.product_name = product_name
        self.added_date = datetime.datetime.utcnow()

    def add_product(self):
        return {
            'productID': str(self.product_id.int)[:5],
            'productName': self.product_name,
            'productQuantity': self.product_quantity,
            'productprice': self.product_price,
            'dateAdded': self.added_date
        }

    def get_products(self):
        return [
         {
            'productID': str(self.product_id.int)[:5],
            'productName': self.product_name,
            'productQuantity': self.product_quantity,
            'productprice': self.product_price,
            'dateAdded': self.added_date
            }
        ]

    def delete_product(self, Prod):
        pass

    class ValidateProducts:

        def validate_input_data(self, request_data):
            """
            Validates input data from the new product form
            Args:
                request_data(object): request Object that holds form data
            Retruns:
                dict: {"errors", True} for no errors {"", False} if errors present
            """
            errors = {}
            if not request_data["product_name"].strip():
                errors.update({"product_name": "Product name is required"})

            if not request_data["product_price"]:
                errors.update({"product_price": "Product price is required"})

            if request_data.get("product_quantity") and not request_data["qty"]:
                errors.update({"product_quantity": "Quantity is required"})

            return {
                "errors": errors,
                "is_true": empty_field(self, errors)
            }

    def validate_number_fields(self, request_data):
        errors = {}
        try:
            if request_data.get("product_quantity"):
                int(request_data.get("product_quantity"))

            if request_data.get("product_price"):
                int(request_data.get("product_price"))
        except ValueError:
            errors.update(
                {"value": "Only numbers allowed for both price and quantity"})

        return {
            "errors": errors,
            "is_true": empty_field(self, errors)
        }