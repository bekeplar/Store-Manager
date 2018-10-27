import datetime
import uuid
from flask import jsonify
from api.models.validation import empty_field


class Sales:

    '''
    The sales are a list of sales created in the store.
    '''

    def __init__(
        self, product_name,
        product_price,
        product_quantity,
        customer_name
            ):
        self.sale_id = uuid.uuid4()
        self.product_quantity = product_quantity
        self.product_price = product_price
        self.product_name = product_name
        self.customer_name = customer_name
        self.added_date = datetime.datetime.utcnow()
        '''
         sale_id and date will be created automatically.
        '''

    def add_Sale(self):
        return {
            'saleID': str(self.sale_id.int)[:5],
            'productName': self.product_name,
            'productQuantity': self.product_quantity,
            'productprice': self.product_price,
            'dateAdded': self.added_date,
            'customerName': self.customer_name
            }

    def get_sales(self):
        return [
         {
            'saleID': str(self.sale_id.int)[:5],
            'productName': self.product_name,
            'productQuantity': self.product_quantity,
            'productprice': self.product_price,
            'dateAdded': self.added_date,
            'customerName': self.customer_name
            }
        ]

    def get_sale_by_id(self, id):
        pass


class ValidateStockInput:

    def validate_input_data(self, request_data):
        """
        Validates input data from the new stock form
        Args:
            request_data(object): request Object that holds form data
        Retruns:
            dict: {"errors", True} for no errors {"", False} if errors present
        """
        errors = {}
        try:
            if not request_data["product_id"]:
                errors.update({"id": "Please select a product"})

            if not request_data["quantity"]:
                errors.update({"quantity": "Quantity is required"})

            int(request_data["quantity"])
        except ValueError:
            errors.update({"quantity": "Only numbers allowed for quantity"})

        return {
            "errors": errors,
            "is_true": empty_field(self, errors)
        }    