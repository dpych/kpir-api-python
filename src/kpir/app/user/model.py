from kpir.core import db, CoreModel, Config
from datetime import datetime
import uuid

__author__ = "Dawid Pych <dawidpych@gmailcom>"
__date__ = "$2015-08-31 14:21:46$"


class Users(db.Model, CoreModel):
    name = db.Column(db.String(255), index=True, nullable=False)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(255), nullable=False)
    roles = db.relationship('Roles', secondary='users_roles', backref=db.backref('users', lazy='dynamic'))
    session = db.relationship('Session', backref='users', lazy='dynamic')

    def login(self):
        return self.session.create_token()

    def logout(self):
        self.session.delete_token()

    def check_login(self):
        self.session.check_token()


class UsersRoles(db.Model):
    __tablename__ = 'users_roles'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)


class Roles(db.Model, CoreModel):
    name = db.Column(db.String(255), index=True, nullable=False)


class Session(db.Model, CoreModel):
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    uuid = db.Column(db.String(255), index=True, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)

    def create_token(self):
        token = uuid.uuid4()
        time = datetime.now()
        data = dict(user_id=self.id, uuid=token, update_time=time)
        self.add_row(data)
        return self.uuid

    def check_token(self):
        time = datetime.now()

        if time <= self.uuid + Config.get('SESSION','LIFE'):
            self.update_time = time
            return True
        else:
            self.delete_row(self.id)

        return False

    def delete_token(self):
        self.delete_row(self.id);
