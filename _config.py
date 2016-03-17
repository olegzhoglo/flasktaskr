import os

#folder where this script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
CSRF_ENABLED = True #helps prevent cross-site request forgery
SECRET_KEY = '\xf4\xd0\x89\xda\xc5q\x9d{\x19\t\x15\xf2\x16\x98\xda\xa8\xd1\xfc\xc7\x15\xd7\xee[\x80'

#path to DB:
DATABASE_PATH = os.path.join(basedir, DATABASE)

#database url
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
