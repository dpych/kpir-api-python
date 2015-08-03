__author__ = "Dawid Pych <dawidpych@gmailcom>"
__date__ = "$2015-08-03 10:31:00$"

from kpir import core
from flask.ext.testing import TestCase

class BaseTestCase(TestCase):
    """
    A base test case for KPIR-API
    """
    
    def create_app(self):
        core.app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///:memory:',
            DEBUG=True,
            TESTING = True
        )
        return core.app
    
    def setUp(self):
        core.db.create_all()
        
    def tearDown(self):
        core.db.session.remove()
        core.db.drop_all()