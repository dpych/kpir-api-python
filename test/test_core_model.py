__author__ = 'Dawid Pych <dawidpych@gmail.com>'
__date__ = '25.07.2015'

from abc import ABCMeta

from kpir import core
from test_base import BaseTestCase


class CoreModel(BaseTestCase):

    coreModel = None

    def setUp(self):
        class TestCoreModelClass(core.CoreModel):
            __name__ = 'TestCoreModelClass'

        self.coreModel = TestCoreModelClass()

    def test_attribute_metaclass(self):
        metaclass = self.coreModel.__metaclass__
        self.assertEqual(metaclass, ABCMeta)

    def test_attribute_metaclass(self):
        table = self.coreModel.__table__
        self.assertEqual(str(table), 'testcoremodelclass')

    def test_attribute_id_exist(self):
        obj = self.coreModel
        self.assertTrue(hasattr(obj, 'id'))

    def test_attribute_params_exists(self):
        obj = self.coreModel
        self.assertTrue(hasattr(obj, 'params'))

    def test_attribute_id_is_column(self):
        ids = self.coreModel.id
        self.assertEqual(str(type(ids)), "<class 'sqlalchemy.schema.Column'>")

    def test_attribute_id_is_column_integer(self):
        ids = self.coreModel.id.type
        self.assertEqual(str(type(ids)), "<class 'sqlalchemy.types.Integer'>")

    def test_attribute_id_column_is_primary_key(self):
        ids = self.coreModel.id.primary_key
        self.assertTrue(ids)

    def test_attribute_params_is_column(self):
        params = self.coreModel.params
        self.assertEqual(str(type(params)), "<class 'sqlalchemy.schema.Column'>")

    def test_rename_tablename_to_lower(self):
        name = self.coreModel.__tablename__
        self.assertEqual(str(name), 'testcoremodelclass')

    def test_get_params(self):
        class TestCoreModelClass(core.CoreModel):
            __name__ = 'TestCoreModelClass'
            params = '{"data":"test"}'

        coreModel = TestCoreModelClass()

        params = coreModel.get_params()
        self.assertEqual(params['data'], "test")

    def test_serialize(self):

        class TestClassModel(core.db.Model, core.CoreModel):
            pass

        core.db.create_all()

        testClass = TestClassModel(id=1, params='{"test":1}')

        ser = testClass.serialize

        self.assertEqual(ser['id'], 1)
        self.assertEqual(ser['params'], dict(test=1))


    def test_add_row(self):

        class TestClassModel2(core.db.Model, core.CoreModel):
            pass

        core.db.create_all()

        testClass = TestClassModel2()

        testClass.add_row(dict(id=2))

        ser = testClass.serialize

        self.assertEqual(ser['id'], 2)
        self.assertIsNone(ser['params'])

    def test_edit_row(self):

        class TestClassModel3(core.db.Model, core.CoreModel):
            pass

        core.db.create_all()

        testClass = TestClassModel3()

        testClass.add_row(dict(id=2, params='{}'))
        testClass.edit_row(dict(id=2, params='{test: 1}'))

        testClass = TestClassModel3.query.get(2)

        ser = testClass.serialize

        self.assertEqual(ser['id'], 2)
        self.assertEqual(ser['params'], '{test: 1}')

    def test_edit_row(self):

        class TestClassModel3(core.db.Model, core.CoreModel):
            pass

        core.db.create_all()

        testClass = TestClassModel3()

        testClass.add_row(dict(id=2, params='{}'))
        testClass.delete_row(2)

        testClass = TestClassModel3.query.get(2)

        self.assertIsNone(getattr(testClass, 'id', None))
        self.assertIsNone(getattr(testClass, 'params', None))

if __name__ == '__main__':
    unittest.main()
