from core import jsonify, db

__author__ = "Dawid Pych <dawidpych@gmailcom>"
__date__ = "$2015-07-05 14:07:00$"

class Model ():
    def get_params(self):
        return jsonify(self.params)
