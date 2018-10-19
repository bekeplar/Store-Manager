from flask import jsonify, request,  url_for
from api import sm, models


@sm.route('/api/v1/admin/product', methods=['POST'])
def add_product():
    parsejson = request.get.json()
    product_name = parsejson['product_name']
    product_id = parsejson['product_id']
    product_price = parsejson['product_price']
    product_quantity = parsejson['product_quantity']
    products.add_product(
        product_name,
        product_id,
        product_price,
        product_quantity
         )
    return jsonify({'message': 'Product has been added'}), 201
