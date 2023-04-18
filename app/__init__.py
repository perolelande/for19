from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
import flask

application = Flask(__name__)

### Code GitHub
application.config['SECRET_KEY'] = "80e49e4bea0c03d64cc40d37f11535b85e93880b43c8c053"

DBVAR = 'postgresql://postgres:FOR19postgres@awseb-e-w5jetrp9pk-stack-awsebrdsdatabase-uyx5nesvp7xx.cmz3f7khsk6s.eu-north-1.rds.amazonaws.com:5432/ebdb'
application.config['SQLALCHEMY_DATABASE_URI'] = DBVAR 
application.config['SQLALCHEMY_BINDS'] ={'transport': DBVAR}

### Code computer
# application.config['SECRET_KEY'] = '3oueqkfdfas8ruewqndr8ewrewrouewrere44554'
# DBVAR = 'sqlite:///user.db'
# application.config['SQLALCHEMY_DATABASE_URI'] = DBVAR
# application.config['SQLALCHEMY_BINDS'] ={'transport': 'sqlite:///transport.db'}

db = SQLAlchemy(application)
bcrypt = Bcrypt(application)
login_manager= LoginManager(application)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

from app.home.routes import home
from app.methodology.routes import methodology
from app.carbon_app.routes import carbon_app
from app.users.routes import users

application.register_blueprint(home)
application.register_blueprint(methodology)
application.register_blueprint(carbon_app)
application.register_blueprint(users)

@application.errorhandler(404)
def error(e):
    return flask.render_template('404.html') 