import datetime

from flask import Flask

#
SECRET_KEY = 'YiANN9FF'
PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=8)


# Database
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'defectdb'
USERNAME = 'root'
PASSWORD = '123456'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = Flask

# Mail  HBtCgQNGbn6ttudB
MAIL_SERVER = 'smtp.163.com'
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = 'yanggeol@163.com'
MAIL_PASSWORD = 'HBtCgQNGbn6ttudB'
MAIL_DEFAULT_SENDER = 'yanggeol@163.com'


# File
UPLOAD_FOLDER = 'static/file'
