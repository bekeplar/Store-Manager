from flask import jsonify, json, request,  url_for, abort
from api import sm
from .models.products import Products
from .models.sales import Sales

"""
These lists will store the Sales and Products.
"""

Prod = []
Sale = []
User = []


@sm.route('/signup', methods=['GET'])
def register_user():
    return jsonify({"Welcome": "Please contact admin"})


@sm.route('/login', methods=['POST'])
def user_login():
    data = request.json

    username = data['username']
    password = data['password']

    if not username or not password:
        abort(400)

        return jsonify({"Success": "User Logged in successfuly"}), 200


@sm.route('/', methods=['GET'])
def home():
    return jsonify({"Welcome": "Welcome to my Store"})

    """
    Endpoint for adding a product to the store.
    """


@sm.route('/api/v1/products', methods=['POST'])
def add_product():
    data = json.loads(request.data)
    product_name = data['product_name']
    product_price = data['product_price']
    product_quantity = data['product_quantity']
    if not request.content_type == 'application/json':
        return jsonify({'error': 'unsupported content-type'}), 400
    if ("" in product_name) == True:
            return jsonify({'error': 'enter product name'})
    product = Products(product_name, product_price, product_quantity)
    Prod.append(product.add_product())
    return jsonify({'msge': 'success'}), 201


@sm.route('/api/v1/products', methods=['GET'])
def get_all_products():
    '''
    This function returns a list of all products in the store.
    '''
    if len(Prod) == 0:
        return jsonify({'error': 'Store is out of stock'}), 404
    return jsonify({'Stock Available': Prod}), 200
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
    if not request.content_type == 'application/json': 
        return jsonify({'error': 'Wrong content-type'}), 400
    if len(Sale) == 0:
        return jsonify({'error': 'No sales made yet'}), 404
    sales = Sales(product_name, product_price, product_quantity, customer_name)
    Sale.append(sales.add_Sale())
    return jsonify({'msg': 'business progressing'}), 201


@sm.route('/api/v1/products/<product_id>', methods=['GET'])
def get_a_specific_product(id):
    '''
    This function gets a specific item by its id.
    '''
    if len(Products) == 0:
            return jsonify({'error': 'The store is short of stock'}), 404 
    for product_item in Prod:
        if product_item['product_id'] == id:
            return jsonify({'result': Prod}), 200
    return jsonify({'error': 'Product not in stock'}), 404


@sm.route('/api/v1/sales', methods=['GET'])
def get_all_sales():
    '''
     Function to enable an admin get all sales records.
    '''
    if len(Products) == 0:
            return jsonify({'error': 'The store is short of stock'}), 404
    return jsonify({'Sales': Sales, 'msg': 'You own it'}), 200
