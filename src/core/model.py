from core import jsonify, db
from sqlalchemy.ext.declarative import declared_attr

__author__ = "Dawid Pych <dawidpych@gmailcom>"
__date__ = "$2015-07-05 14:07:00$"

"""
Defauld model for all new models in app 
"""

class CoreModel (object):
    id = db.Column(db.Integer, primary_key=True)
    params = db.Column(db.Text)
    __table__ = None
    
    def __init__(self):
        super(self)
        self.__table__ = self.__name__.lower()
    
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    def get_params(self):
        return jsonify(self.params)