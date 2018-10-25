import unittest
from unittest import TestCase
from api import sm
from api import views
from api.models.products import Products
from api.models.sales import Sales


import json

product = {
    "product_name": "Boots",
    "product_price": "80000UGX",
    "product_quantity": 4
}

Invalid_input = {
    "product_name": "Boots",
    "product_price": "80000UGX",
    "product_quantity": 'zzz'
}

Missing_name = {
    "product_name": "",
    "product_price": "80000UGX",
    "product_quantity": 22
}

No_quantity = {
    "product_name": "Boots",
    "product_price": "80000UGX",
    "product_quantity": ""
}


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
   
    def tearDown(self):
        self.testclient = sm.test_client()
        """
        Deleting our test samples after testing is done
        """

