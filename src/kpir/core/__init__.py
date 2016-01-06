"""
Core module for KPIR API Server
"""
__author__ = "Dawid Pych <dawidpych@gmailcom>"
__date__ = "$2015-07-11 14:55:09$"

import sys
import os

sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from flask import Flask, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from kpir.core.config import Config
from kpir.core.controller import not_found
import os.path

app = Flask(__name__)

"""
Config import
"""
app.config.from_object('config')

"""
Override 404
"""
app.error_handler_spec[None][404] = not_found

"""
Initiatie database SQLAlchemy
"""
db = SQLAlchemy(app)

"""
Abstract Model for table
"""
from kpir.core.model import CoreModel

"""
Import app modules
"""
for model in Config.get('MODULES','LIST').split(','):
    if model:
       module = __import__('kpir.app.' + model, fromlist=['model', 'controller'])
