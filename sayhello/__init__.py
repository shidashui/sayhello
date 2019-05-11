#__author__ = 'shidashui'

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask('sayhello')


db = SQLAlchemy(app)
