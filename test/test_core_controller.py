import core
from test_base import BaseTestCase
from flask import json


class CoreController_TestCase(BaseTestCase):

    def test_response(self):
        model = {
            'data': 'succes_test',
            'data1': 'success_test2'
        }

        resp = core.controller.response(model, 200)
        data = json.loads(resp.data)

        self.assert200(resp, 200)
        self.assertEqual(data['data']['data'], model['data'])
        self.assertEqual(data['data']['data1'], model['data1'])
        self.assertEqual(data['page'], 1)
        self.assertEqual(data['length'], 1000)
        self.assertTrue(data['success'])


    def test_not_found(self):
        test = core.app.test_client()
        resp = test.get('/')
        data = json.loads(resp.data)

        self.assert404(resp)
        self.assertEqual(data["status"], 404)
        self.assertEqual(data["message"], 'Not Found: ' + core.request.url)


if __name__ == '__main__':
    unittest.main()

