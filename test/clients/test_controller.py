from flask import json
import kpir.core as core
from test_base import BaseTestCase

__author__ = 'Dawid Pych <dawidpych@gmail.com>'
__date__ = '08.08.2015'


class ClientController_TestCase(BaseTestCase):
    def test_clients(self):
        rp = self.client.get('/clients/')

        self.assert200(rp)

    def test_clients_query(self):
        rp = self.client.get('/clients/?page=5&limit=2')
        data = json.loads(rp.data)

        self.assert200(rp)
        self.assertEqual(data['page'], 5)

    def test_method_get_only_clients(self):
        get = self.client.get('/clients/')
        post = self.client.post('/clients/')
        put = self.client.put('/clients/')
        delete = self.client.delete('/clients/')

        self.assert200(get)
        self.assert405(post)
        self.assert405(put)
        self.assert405(delete)

    def test_clients_is_data(self):
        rp = self.client.get('/clients/')
        self.assertIsNotNone(rp.data)

    def test_clients_default_data(self):
        rp = self.client.get('/clients/')
        data = json.loads(rp.data)

        self.assertTrue(data['success'])
        self.assertIsNotNone(data['length'])
        self.assertIsNotNone(data['page'])
        self.assertIsNotNone(data['data'])

    def test_clients_data(self):
        rp = self.client.get('/clients/')
        data = json.loads(rp.data)

        self.assertIsNotNone(data['data']['clients'])
        self.assertEqual(type(data['data']['clients']), list)

    def test_get_client(self):
        rp = self.client.get('/client/1')

        self.assert200(rp)

    def test_post_create_client(self):
        rp = self.client.post('/client/')

        self.assert403(rp)

    def test_post_client(self):
        rp = self.client.post('/client/1')

        self.assert405(rp)

    def test_put_client(self):
        rp = self.client.put('/client/1')

        self.assert200(rp)

    def test_delete_client(self):
        rp = self.client.delete('/client/1')

        self.assert200(rp)
