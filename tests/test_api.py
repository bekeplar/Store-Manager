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
        self.assertEqual(res.status_code, 201)


class ProductsTestCase(TestCase):

    def setUp(self):
        self.testclient = sm.test_client()

    def test_add_product(self):
        response = self.testclient.post(
            '/api/v1/products',
            content_type="application/json",
            data=json.dumps(product))
        self.assertEqual(response.status_code, 201)
        self.assertIn("The product has been added", response.data)

        """
        Testing for invalid and missing inputs.
        """

    def test_get_all_products(self):
        result = self.testclient.get('/api/v1/products')
        self.assertEqual(result.status_code, 200)    

    def test_add_product_invalid_input(self):
        response = self.testclient.post(
            '/api/v1/products',
            content_type="application/json",
            data=json.dumps(Invalid_input))
        self.assertEqual(response.status_code, 400)
        self.assertIn("Server Error, Check product input", response.data)

    def test_add_product_Missing_input(self):
        response = self.testclient.post(
            '/api/v1/products',
            content_type="application/json",
            data=json.dumps(Missing_name))
        self.assertEqual(response.status_code, 400)
        self.assertIn("Server Error, Check product input", response.data)

    def test_add_product_with_no_quantity(self):
        response = self.testclient.post(
            '/api/v1/products',
            content_type="application/json",
            data=json.dumps(No_quantity))
        self.assertEqual(response.status_code, 400)
        self.assertIn("Server Error, Check Quantity input", response.data)   

    def test_get_a_specific_product(self):
        result = self.testclient.get('/api/v1/products/<product_id>')
        self.assertEqual(result.status_code, 200)

    def tearDown(self):
        self.testclient = sm.test_client()
        """
        Deleting our test samples after testing is done
        """

