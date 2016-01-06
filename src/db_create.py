#!/usr/bin/python3

__author__ = "Dawid Pych <dawidpych@gmailcom>"
__date__ = "$2015-07-05 14:16:38$"

import os.path

from kpir.core.config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, Config
from kpir.core import db
from migrate.versioning import api

db.create_all()
db.session.commit()

if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
    api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
else:
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))