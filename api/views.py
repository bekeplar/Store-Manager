from flask import jsonify, json, request,  url_for
from api import sm
from .models.products import Products
from .models.sales import Sales

"""
These lists will store the Sales and Products.
"""

Prod = []
Sale = []
"""
Endpoint for adding a product to the store.
"""


@sm.route('/api/v1/products', methods=['POST'])
def add_product():
    data = json.loads(request.data)
    product_name = data['product_name']
    product_price = data['product_price']
    product_quantity = data['product_quantity']
    product = Products(product_name, product_price, product_quantity)
    Prod.append(product.add_product())
    return jsonify({'msge': 'success'}), 201
"""
Endpoint for accessing a product from the store,
"""


@sm.route('/api/v1/products', methods=['GET'])
def get_all_products():
    '''
    This function returns a list of all products in the store.
    '''
    return jsonify({
        'products': Prod}), 200

"""
Endpoint for adding a sale to the store/Attendant.
"""


@sm.route('/api/v1/sales', methods=['POST'])
def add_sale():
    '''
    This function enables a store attendant to add sale
    order to the list of orders.
    '''
    data = json.loads(request.data)
    product_name = data['product_name']
    customer_name = data['customer_name']
    product_price = data['product_price']
    product_quantity = data['product_quantity']
    sales = Sales(product_name, product_price, product_quantity, customer_name)
    Sale.append(sales.add_Sale())
    return jsonify({'msge': 'success'}), 201


@sm.route('/api/v1/products/product_id', methods=['GET'])
def get_a_specific_product(id):
    '''
    This function gets a specific item by its id.
    '''
    return jsonify({'product': get_a_specific_product(id)}), 200


@sm.route('/api/v1/admin/sales', methods=['GET'])
def get_all_sales():
    '''
     Function to enable an admin get all sales records.
    '''
    return jsonify({'Sales': Sales, 'msg': 'he'}), 200

