from flask import json

import kpir.core as core
from test_base import BaseTestCase


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

    def test_crud(self):
        class TestModel(core.db.Model, core.CoreModel):
            name = core.db.Column(core.db.String(64))

        model = TestModel

        @core.app.route('/test/<int:id>', methods=['GET', 'PUT', 'DELETE'])
        @core.app.route('/test/', methods=['POST'], defaults={'id': None})
        def test(id):
            return core.controller.crud(model=model, id=id)

        core.db.create_all()

        r = core.app.test_client()

        post = r.post('/test/', data=json.dumps(dict(params={'test': True}, name="test1")), content_type='application/json')
        get = r.get('/test/1')
        put = r.put('/test/1', data=json.dumps(dict(params={'test': False}, name="test2")), content_type='application/json')
        delete = r.delete('/test/1')

        post = json.loads(post.data)
        get = json.loads(get.data)
        put = json.loads(put.data)
        delete = json.loads(delete.data)

        self.assertEqual(post['data']['id'], 1)
        self.assertTrue(post['success'])
        self.assertEqual(post['page'], 1)
        self.assertEqual(post['length'], 1)

        self.assertEqual(get['data']['id'], 1)
        self.assertTrue(get['success'])
        self.assertEqual(get['page'], 1)
        self.assertEqual(get['length'], 1)

        self.assertEqual(put['data']['name'], 'test2')
        self.assertEqual(put['data']['params'], dict(test=False))

        self.assertEqual(delete['data']['action'], dict(remove=True))
        self.assertEqual(delete['length'], 0)

if __name__ == '__main__':
    unittest.main()

