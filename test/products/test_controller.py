from flask import json
import kpir.core as core
from test_base import BaseTestCase

__author__ = 'Dawid Pych <dawidpych@gmail.com>'
__date__ = '08.08.2015'


class ProductController_TestCase(BaseTestCase):
    def test_clients(self):
        rp = self.client.get('/products/')

        self.assert200(rp)

    def test_clients_query(self):
        rp = self.client.get('/products/?page=5&limit=2')
        data = json.loads(rp.data)

        self.assert200(rp)
        self.assertEqual(data['page'], 5)

    def test_method_get_only_clients(self):
        get = self.client.get('/products/')
        post = self.client.post('/products/')
        put = self.client.put('/products/')
        delete = self.client.delete('/products/')

        self.assert200(get)
        self.assert405(post)
        self.assert405(put)
        self.assert405(delete)

    def test_clients_is_data(self):
        rp = self.client.get('/products/')
        self.assertIsNotNone(rp.data)

    def test_clients_default_data(self):
        rp = self.client.get('/products/')
        data = json.loads(rp.data)

        self.assertTrue(data['success'])
        self.assertIsNotNone(data['length'])
        self.assertIsNotNone(data['page'])
        self.assertIsNotNone(data['data'])

    def test_clients_data(self):
        rp = self.client.get('/products/')
        data = json.loads(rp.data)

        self.assertIsNotNone(data['data']['products'])
        self.assertEqual(type(data['data']['products']), list)

    def test_get_client(self):
        rp = self.client.get('/product/1')

        self.assert200(rp)

    def test_post_create_client(self):
        rp = self.client.post('/product/')

        self.assert403(rp)

    def test_post_client(self):
        rp = self.client.post('/product/1')

        self.assert405(rp)

    def test_put_client(self):
        rp = self.client.put('/product/1')

        self.assert200(rp)

    def test_delete_client(self):
        rp = self.client.delete('/product/1')

        self.assert200(rp)
