"""
Default abstract models for models in app.
"""
from abc import ABCMeta
import json
from sqlalchemy.ext.declarative import declared_attr
from kpir.core import db

__author__ = "Dawid Pych <dawidpych@gmailcom>"
__date__ = "$2015-07-05 14:07:00$"


class CoreModel(object):
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

    def __init__(self, model=None):
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

    def __repr__(self):
         return '<%s %r>' % (self.__class__.__name__, self.name)

    def get_params(self):
        """
        Convert json params to dictionary.
        :return:
        """
        return json.loads(self.params)

    @property
    def serialize(self):
        """
        Serialize model
        :return:
        """
        ret = {}
        for column in self.__table__.columns:
            if column.name == 'params' and getattr(self, column.name) and getattr(self, column.name) != '':
                ret[column.name] = json.loads(getattr(self, column.name, '{}'))
            else:
                ret[column.name] = getattr(self, column.name)
        return ret

    def add_row(self, data):
        """
        Method to add new row

        :param dict data:
        :return object:
        """
        if data:
            save = True

            for k in self.__table__.columns:
                name = getattr(k, 'name')
                required = not getattr(k, 'nullable')
                if name in data:
                    if name == 'params':
                        setattr(self, name, json.dumps(data.get(name)))
                    else:
                        setattr(self, name, data.get(name))
                else:
                    if required and name != 'id':
                        save = False

            if save:
                db.session.add(self)
                db.session.commit()

        return self

    def edit_row(self, data):
        """
        Edit row

        :param dict data:
        :return object:
        """
        if data:
            save = True

            for k in self.__table__.columns:
                name = getattr(k, 'name')
                required = not getattr(k, 'nullable')

                if name in data:
                    if name == 'params':
                        setattr(self, name, json.dumps(data.get(name)))
                    else:
                        setattr(self, name, data.get(name))
                else:
                    if required:
                        save = False
            if save:
                db.session.commit()

        return self

    def delete_row(self, id):
        """
        Remove row

        :param int id:
        :return bool:
        """
        if id:
            self.query.get(int(id))
            if self.id:
                db.session.delete(self)
                db.session.commit()
                return True
            else:
                return False
        else:
            return False
