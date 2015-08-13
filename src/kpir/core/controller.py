"""
Controller Core.
"""
from flask import request, jsonify, json

__author__ = "Dawid Pych <dawidpych@gmailcom>"
__date__ = "$2015-07-05 15:32:20$"


def response(response={}, status=200, mimetype=None, page=1, lenght=1000):
    """
    Generate default json resonse for controller.
    :param response: data to return in request
    :param status: code of response example : 200 it`s mean response OK
    :param mimetype:
    :param page: information of with page of data is return
    :param lenght: how meny page is with data
    :return:
    """
    if status == 200:
        success = True
    else:
        success = False

    response = {
        "data": response,
        "success": success,
        "page": page,
        "length": lenght
    }

    response = jsonify(response)
    response.status_code = status

    return response


def not_found(error=None):
    """
    Default error return.
    :param error:
    :return:
    """
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp


def crud(model, id):

    if request.data:
        s = json.loads(request.data)
    else:
        s = None

    if request.method == 'GET':
        model = model.query.get(id)
        return response(response=model, lenght=(getattr(model, 'id', False) if 1 else 0))
    elif request.method == 'POST':
        model = model().add_row(s)
        return response(model.serialize)
    elif request.method == 'PUT':
        if s:
            s['id'] = id
        model = model().edit_row(s)
        return response(response=model.serialize, lenght=0)
    elif request.method == 'DELETE':
        if id:
            ret = model().delete_row(id)
        else:
            ret = False
        return response({'action': {'remove': ret}}, lenght=0)