__author__ = "Dawid Pych <dawidpych@gmailcom>"
__date__ = "$2015-07-11 14:55:09$"

from flask import Flask, jsonify, request
from flask.ext.sqlalchemy import SQLAlchemy
from core.config import Config, SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO
from core.controller import response, not_found

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

from core.model import Model