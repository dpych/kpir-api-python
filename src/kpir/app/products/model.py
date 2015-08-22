from kpir.core import db, CoreModel

__author__ = "Dawid Pych <dawidpych@gmailcom>"
__date__ = "$2015-08-19 13:56:58$"


class Products(db.Model, CoreModel):
    name = db.Column(db.String(255), index=True, nullable=False)
    sku = db.Column(db.String(64), unique=True)
    price = db.Column(db.Float, nullable=False)
    tax = db.Column(db.Integer(3), nullable=False)
    jm = db.Column(db.String(24))