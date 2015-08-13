from kpir.core import db, CoreModel

__author__ = "Dawid Pych <dawidpych@gmailcom>"
__date__ = "$2015-07-05 13:56:58$"


class Clients(db.Model, CoreModel):
    name = db.Column(db.String(255), index=True, unique=True, nullable=False)

    shortname = db.Column(db.String(64), index=True, unique=True)

    nip = db.Column(db.Integer(11), nullable=False)

    address = db.Column(db.String(255))

    zip = db.Column(db.String(3))

    country = db.Column(db.String(3))