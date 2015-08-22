__author__ = "Dawid Pych <dawidpych@gmailcom>"
__date__ = "$2015-07-05 12:21:46$"

from kpir.core import app, request
from kpir.core.controller import response, crud
from kpir.app.products.model import Products


@app.route('/products/', methods=['GET'])
def products():
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 100))
    model = Products.query.limit(limit).offset((1 - page)*limit).all()

    return response(response={'products': [i.serialize for i in model]}, lenght=len(model), page=page)


@app.route('/product/<int:id>', methods=['GET', 'PUT', 'DELETE'])
@app.route('/product/', methods=['POST'], defaults={'id': None})
def product(id):
    model = Products
    return crud(model, id)