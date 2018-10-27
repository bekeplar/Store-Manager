import unittest
from unittest import TestCase
from api import sm
from api import views
from api.models.sales import Sales
from api.models.products import Products
from api.models.validation import empty_field
import json


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        """
        This method executes before each test run
        """
        self.api = sm.test_client(self)

    def test_post(self):
        with self.api as client:
            res = client.post('/api/v1/products', json=dict(product_name="boots", product_price=1000, product_quantity=2))
            self.assertEqual(res.status_code, 201)


class ProductsTestCase(TestCase):

    def setUp(self):
        self.testclient = sm.test_client()

    def test_home_route(self):
        response = self.testclient.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to my Store', response.data)

    def test_add_product(self):
        product = {
            "product_name": "Boots",
            "product_price": "8000.00",
            "product_quantity": 6
        }

        result = self.testclient.post('/api/v1/products', content_type='application/json', data=json.dumps(product))
        self.assertEqual(result.status_code, 201)                      

    def test_get_all_products(self):
        response = self.testclient.get('/api/v1/products')
        self.assertIn(b'Stock Available', response.data)


class SalesTestCase(TestCase):

    def setUp(self):
        self.testclient = sm.test_client()

    def test_get_all_sales(self):
        response = self.testclient.get('/sales')
        self.assertIn(b'You own it', response.data)

    def tearDown(self):
        self.testclient = sm.test_client()
        """
        Deleting our test samples after testing is done
        """
