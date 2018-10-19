import pytest
from datetime import datetime
from flask import Response, json
from api import sm, routes, models, status


def test_index():
    user = sm.test_user()
    res = user.get('/')
    assert res.status_code == status.HTTP_200_OK


def test_add_product():
    admin = sm.test_admin()
    res = admin.post('/api/v1/admin/product', json={
        'product_name': 'Boots',
        'product_price': '50k UGX', 
        'product_quantity': '12',
        'product_id': '1'
        })
    assert res.status_code == 201


def test_get_a_specific_product():
    admin = sm.test_admin()
    res = admin.get('/api/v1/products/product_id')
    assert res.status_code == status.HTTP_200_OK


def test_add_sale():
    attendant = sm.test_attendant()
    res = attendant.post('/api/v1/attendant/sales', json={
        'product_name': 'Boots',
        'product_quantity': 2,
        'product_price': '100K UGX',
        'customer_name': 'bekeplar',
        'sale_id': '1'
    })
    assert res.status_code == status.HTTP_201_CREATED


def get_all_products():
    user = sm.test_user()
    res = user.get('/api/v1/products')
    assert res.status_code == status.HTTP_200_OK


def test_get_all_sales():
    admin = sm.test_admin()
    res = admin.get('/api/v1/admin/sales')
    assert res.status_code == status.HTTP_200_OK
