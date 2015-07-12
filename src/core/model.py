from core import jsonify, db, declared_attr

__author__ = "Dawid Pych <dawidpych@gmailcom>"
__date__ = "$2015-07-05 14:07:00$"

"""
Defauld model for all new models in app 
"""

class CoreModel (object):
    id =  db.Column(db.Integer, primary_key=True)
    
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    def get_params(self):
        return jsonify(self.params)
