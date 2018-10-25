import datetime
import uuid
from flask import jsonify


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
        pass

    