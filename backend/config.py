import os
from os.path import join, dirname
from dotenv import load_dotenv


#TODO get the dotenv environment to work
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


class Config(object):
    # Default configuration
    APP_ENV = os.environ.get('APP_ENV', 'development')

    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    DEBUG = True
    TESTING = False

    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL'] + os.environ['APP_DB'] + "?client_encoding=utf8"
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ['SQLALCHEMY_TRACK_MODIFICATIONS']