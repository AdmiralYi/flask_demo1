import os
import pymysql
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = 'dev'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1230mmm@localhost:3306/flasktest?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

