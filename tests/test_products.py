from unittest import TestCase
from flask import json, Response, Request
from api import sm
from api.models.products import Products
from api.models.sales import Sales

product = {
    "product_name": "Boots",
    "product_price": "80000UGX",
    "product_quantity": 4
}

invalid_product = {
    "product_name": "Boots",
    "product_price": "80000UGX",
    "product_quantity": 4
}


class ProductsTestCase(TestCase):

    def setUp(self):
        self.testclient = sm.test_client()

    def test_add_product(self):
        response = self.testclient.post('/api/v1/admin/products', content_type="application/json",
                                        data=json.dumps(product))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"The product has been added", response.data)

    def test_add_product_invalid_input(self):
        response = self.testclient.post('/api/v1/admin/products', content_type="application/json",
                                        data=json.dumps(invalid_product))
        self.assertEquals(response.status_code, 500)
        self.assertIn(b"Server Error, Check product input", response.data)
    
 
