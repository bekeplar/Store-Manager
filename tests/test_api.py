import unittest
from unittest import TestCase
from api import sm
from api import views
from api.models.products import Products
from api.models.sales import Sales
import json


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        """
        This method executes before each test run
        """
        self.api = sm.test_client(self)

    def test_post(self):
        res = self.api.post('/api/v1/products', content_type="application/json", data=json.dumps({"product_name": "boots", "product_price": 1000, "product_quantity": 2}))
        self.assertEqual(res.status_code, 200)


class ProductsTestCase(TestCase):

    def setUp(self):
        self.testclient = sm.test_client()

    def test_home_route(self):
        response = self.testclient.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to my Store', response.data)

    def test_add_single_product(self):
        product = {
            "product_name": "Boots",
            "product_price": "8000.00",
            "product_quantity": 6,
        }

        result = self.testclient.post('/api/v1/products', content_type='application/json',
                                  data=json.dumps(product))

    def test_get_all_products(self):
        response = self.testclient.get('/api/v1/products')
        self.assertIn(b'Store is out of stock', response.data)


class SalesTestCase(TestCase):
    def setUp(self):
        self.testclient = sm.test_client()

    def tearDown(self):
        self.testclient = sm.test_client()
        """
        Deleting our test samples after testing is done
        """
