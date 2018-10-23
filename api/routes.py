from flask import jsonify, json, request,  url_for
from . import sm
from flask import request, jsonify
from .models.Products import Products
from .models.sales import Sales
from api.validators import Validators


"""
These lists will store the Sales and Products.
"""
Products = []
Sales = []


@sm.route('/api/v1/admin/product', methods=['POST'])
def add_product():
    parsejson = request.get.json()
    product_name = parsejson['product_name']
    product_id = parsejson['product_id']
    product_price = parsejson['product_price']
    product_quantity = parsejson['product_quantity']
    Products.append(
        product_name,
        product_id,
        product_price,
        product_quantity
         )
    return jsonify({'message': 'Product has been added'}), 201
    

@sm.route('/api/v1/products/product_id', methods=['GET'])
def get_a_specific_product(id):
    '''
    This function gets a specific item by its id.
    '''
    return jsonify({'product': get_a_specific_product(id)}), 200


@sm.route('/api/v1/products', methods=['GET'])
def get_all_products():
    '''
    This function returns a list of all products in the store.
    '''
    return jsonify({
        'products': Products}), 200


@sm.route('/api/v1/admin/sales', methods=['GET'])
def get_all_sales():
    '''
     Function to enable an admin get all sales records.
    '''
    return jsonify({'Sales': Sales, 'msg': 'hey'}), 200


@sm.route('/api/v1/attendant/sales', methods=['POST'])
def add_sale():
    '''
    This function enables a store attendant to add sale
    order to the list of orders.
    '''
    data = request.get_json()
    product_name = data['product_name']
    product_category = data['product_category']
    quantity = data['quantity']
    product_price = data['product_price']
    date_added = data['date_added']
    product_id = data['product_id']
    Attendant_name = data['attendant_name']
    Sales.append(
        product_name,
        product_category,
        product_id,
        quantity,
        product_price,
        date_added,
        Attendant_name
            )
    return jsonify({'message': 'sale successfully added '}), 200
