import core

__author__ = "Dawid Pych <dawidpych@gmailcom>"
__date__ = "$2015-07-05 15:32:20$"

def response(response = {}, status=200, mimetype=None, page=1, lenght=1000):
    if status == 200 :
        success = True;
    else:
        success = False

    response = {
        "data" : response,
        "success" : success,
        "page": page,
        "length": lenght
    }

    response = core.jsonify(response)
    response.status_code = status

    return response


def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + core.request.url,
    }
    resp = core.jsonify(message)
    resp.status_code = 404

    return resp