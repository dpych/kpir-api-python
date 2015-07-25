__author__ = 'Dawid Pych <dawidpych@gmail.com>'
__date__ = '25.07.2015'

import core
from flask.ext.testing import TestCase
from abc import ABCMeta
from flask import json


class CoreModel(TestCase):

    coreModel = None

    def setUp(self):
        class TestCoreModelClass(core.CoreModel):
            __name__ = 'TestCoreModelClass'
            pass
        self.coreModel = TestCoreModelClass()

    def create_app(self):
        return core.app

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

    def test_attribute_params_is_column(self):
        params = self.coreModel.params
        self.assertEqual(str(type(params)), "<class 'sqlalchemy.schema.Column'>")


if __name__ == '__main__':
    unittest.main()
