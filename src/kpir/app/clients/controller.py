__author__ = "Dawid Pych <dawidpych@gmailcom>"
__date__ = "$2015-07-05 12:21:46$"

from kpir.core import app, db, request
from kpir.core.controller import response, crud
from kpir.app.clients.model import Clients
from flask import json, jsonify


@app.route('/clients/', methods=['GET'])
def clients():
    model = Clients.query.all()
    return response(response={'clients': [i.serialize for i in model]}, lenght=len(model))


@app.route('/client/<int:id>', methods=['GET', 'PUT', 'DELETE'])
@app.route('/client/', methods=['POST'], defaults={'id': None})
def client(id):
    model = Clients
    return crud(model, id)