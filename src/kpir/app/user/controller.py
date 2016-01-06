__author__ = "Dawid Pych <dawidpych@gmailcom>"
__date__ = "$2015-08-31 14:21:46$"

from kpir.core import app, request
from kpir.core.controller import response
from kpir.app.user.model import Users, Session
import hashlib


@app.before_request
def token_check():
    token = request.headers.get('token', None);
    if token:
        session = Session.query.filter_by(uuid=token).first()
        session.check_token()


@app.route('/user/login', methods=['POST'])
def login():
    post = request.get_json()

    if getattr(post, 'user') and getattr(post, 'password'):
        user = Users.query.filter_by(name=getattr(post, 'user')).first()
        passwd = hashlib.md5(getattr(post, 'password'))
        passwd = passwd.hexdigest()

        if passwd == user['password']:
            return response(dict(token=user.login(), user=user['id']))

    return response(dict(), 201)


@app.route('/user/logout/<int:id>', methods=['GET'])
def logout(id):
    if id:
        user = Users.query.filter_by(id=id).first()
        user.logout()
        return response(dict(action=True))

    return response(dict(), 201)

def isAuth(func):
    def _decorator(request, *args, **kwargs):
        response = func(request, *args, **kwargs)
        return response
    return wraps(func)(_decorator)

@app.route('/test/', methods=['GET'])
@isAuth
def test():
    print("Test")
