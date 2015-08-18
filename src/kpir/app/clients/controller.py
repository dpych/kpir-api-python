__author__ = "Dawid Pych <dawidpych@gmailcom>"
__date__ = "$2015-07-05 12:21:46$"

from kpir.core import app, db, request
from kpir.core.controller import response, crud
from kpir.app.clients.model import Clients


@app.route('/clients/', methods=['GET'])
def clients():
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 100))
    model = Clients.query.limit(limit).offset((1 - page)*limit).all()

    return response(response={'clients': [i.serialize for i in model]}, lenght=len(model), page=page)


@app.route('/client/<int:id>', methods=['GET', 'PUT', 'DELETE'])
@app.route('/client/', methods=['POST'], defaults={'id': None})
def client(id):
    model = Clients
    return crud(model, id)