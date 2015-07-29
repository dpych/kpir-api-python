"""
Default abstract models for models in app.
"""
from core import db
from sqlalchemy.ext.declarative import declared_attr
from abc import ABCMeta
import json

__author__ = "Dawid Pych <dawidpych@gmailcom>"
__date__ = "$2015-07-05 14:07:00$"


class CoreModel (object):
    """
    Abstract model for template table to use in SQLAlchemy ORM.
    """

    # Declaration of abstract class.
    __metaclass__ = ABCMeta

    # Place for generated table name.
    __table__ = None

    # Default id column for table
    id = db.Column(db.Integer, primary_key=True)

    # Default params column where data are holds in json
    params = db.Column(db.Text)

    def __init__(self):
        """
        Constructor.
        :return:
        """
        self.__table__ = self.__name__.lower()

    @declared_attr
    def __tablename__(cls):
        """
        Return table name write in lowercase
        :param cls:
        :return:
        """
        return cls.__name__.lower()

    def get_params(self):
        """
        Convert json params to dictionary.
        :return:
        """
        return json.loads(self.params)
