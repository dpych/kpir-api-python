import configparser
from core import os

__author__="Dawid Pych <dawidpych@gmailcom>"
__date__ ="$2015-07-05 12:34:07$"

BASE_PATH = os.path.dirname(os.path.realpath(__file__)) + '/../'

file = BASE_PATH + 'config.ini'

Config = configparser.ConfigParser()
Config.read(file)

"""
Database connetion for mysql should looks like:
    For mysql: mysql+mysqldb://mydb_user:mydb_pwd@localhost:3306/mydb
    For sqlite: sqlite:////abs/path/app.db
"""
if Config.get('DATABASE', 'DRIVER').lower() == 'sqlite' :
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + BASE_PATH + 'app.db'
else:
    SQLALCHEMY_DATABASE_URI = Config.get('DATABASE', 'DRIVER') \
        + '://' + Config.get('DATABASE', 'USER') \
        + ':' + Config.get('DATABASE', 'PASSWD') \
        + '@' + Config.get('DATABASE', 'HOST') \
        + '/' + Config.get('DATABASE', 'BASE')

SQLALCHEMY_MIGRATE_REPO = 'db_repository'