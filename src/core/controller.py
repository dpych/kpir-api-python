import core

__author__ = "Dawid Pych <dawidpych@gmailcom>"
__date__ = "$2015-07-05 15:32:20$"


def response(response = {}, status=200, mimetype=None):
    if not mimetype :
        mimetype 
    response = app.jsonify(response)
    response.status_code = status
    return response

def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + app.request.url,
    }
    resp = app.jsonify(message)
    resp.status_code = 404

    return resp