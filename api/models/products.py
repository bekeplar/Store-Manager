import datetime
import uuid
from flask import jsonify


class Products:
    """This class defines the products sold by the store"""
    Product_id = 0

    def __init__(self, product_name,  product_price, product_quantity):
        self.product_id = uuid.uuid4()
        self.product_quantity = product_quantity
        self.product_price = product_price
        self.product_name = product_name
        self.added_date = datetime.datetime.utcnow()

        self.products = []

    def add_product(self):
        self.products.append({
            'productID': str(self.product_id.int)[:5],
            'productName': self.product_name,
            'productQuantity': self.product_quantity,
            'productprice': self.product_price,
            'dateAdded': self.added_date
        })
        return self.products

    def get_products(self):
        if len(self.products) == 0:
            return jsonify({'error': 'Nothing found'}), 404
        return self.products

    def get_product_by_id(self, id):
        for product in self.products:
            if product['product_id'] == id:
                return jsonify({'product': product})

    def delete_products(self, product_id):
        if len(self.products) > 0:
            for product in self.products:
                if product['product_id'] == product_id:
                    self.products.remove(product)
                    return jsonify({'msg': 'Product deleted.'})
juice = Products('lemon', '2000', '100')    
juice.add_product()
print(juice.products)