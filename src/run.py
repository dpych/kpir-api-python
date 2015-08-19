#!/usr/bin/python3
from kpir.core import app, Config

__author__ = "Dawid Pych <dawidpych@gmailcom>"
__date__ = "$2015-07-05 11:42:32$"

if __name__ == "__main__":
    app.run(debug=Config.get('RUN', 'DEBUG'), host=Config.get('RUN', 'HOST'))
