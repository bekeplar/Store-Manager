import datetime
import uuid
from flask import jsonify


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
        pass

    def get_sale_by_id(self, id):
        pass
