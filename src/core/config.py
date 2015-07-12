import configparser

__author__="Dawid Pych <dawidpych@gmailcom>"
__date__ ="$2015-07-05 12:34:07$"

file = 'config.ini'

Config = configparser.ConfigParser()
Config.read(file)

SQLALCHEMY_DATABASE_URI = Config.get('DATABASE','HOST')
SQLALCHEMY_MIGRATE_REPO = 'db_repository'