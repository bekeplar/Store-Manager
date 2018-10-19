from datetime import datetime
"""
These are models for the project
"""


class User:
    """
    Define user structure
    """
    def __init__(self, user_id, username, password, is_admin):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.is_admin = is_admin


class Products:
    """This class defines the products sold by the store"""
    Product_id = 0

    def __init__(self):
        self.products = []

    def add_product(self, kwargs):
        self.product_id = kwargs.get["product_id"]
        self.product_quantity = kwargs.get["product_quantity"]
        self.product_price = kwargs.get["product_price"]
        self.product_name = kwargs.get["product_name"]
        self.added_date_timestamp = kwargs.get["date_added"]
        self.products.append({
            'productID': self.product_id,
            'productName': self.product_name,
            'productQuantity': self.product_quantity,
            'productprice': self.product_price,
            'dateAdded': self.added_date_timestamp
        })
        return self.products

    def get_products(self):
        if len(self.products) == 0:
            message = {'msg': 'store is empty'}
            return self.products
        return self.products

    def get_product_by_id(self, id):
        for product in self.products:
            if product['id'] == id:
                self.products.append(product)

    def delete_products(self):
        if len(self.products) > 0:
            for product in self.products:
                self.products.remove()


class Sales:
    sale_id = 0

    def __init__(self):

        self.sales = []
        self.sale_status = 'pending'
        '''
        The sales are a list of sales created in the store.
        '''

    def add_sale(self, **kwargs):

        '''
         sale_id will be created automatically.
         '''
        self.__class__.sale_id += 1
        self.product_name = kwargs.get("product_name")
        self.customer_name = kwargs.get("customer_name")
        self.product_quantity = kwargs.get("product_quantity")
        self.product_price = kwargs.get("product_price")
        self.sale_date_timestamp = kwargs.get("sale_date")
        self.sale_id = kwargs.get("sale_id")
        self.sales.append({
            'saleID': self.sale_id,
            'productName': self.product_name,
            'productQuantity': self.product_quantity,
            'productprice': self.product_price,
            'customerName': self.customer_name,
            'saleStatus': self.sale_status,
            'saleDate': self.sale_date_timestamp

        })

    def get_sales(self):
        if len(self.sales) > 0:
            return self.sales

    def get_sale_by_id(self, id):
        for sale in self.sales:
            if sale['id'] == id:
                self.sales.append(sale)
        if len(self.sales) > 0:
            return self.sales
