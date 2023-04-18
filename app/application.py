import flask 
from flask import request, flash, session 
#from db import User, Users
import os
from models import db, User, Transport
from flask_bcrypt import Bcrypt
import flask_login
from flask_session import Session

application = flask.Flask(__name__)

application.secret_key = "80e49e4bea0c03d64cc40d37f11535b85e93880b43c8c053"
DEV_PORT = 5000
PRO_PORT = 80

DEV_HOST = "localhost"
PRO_HOST = "0.0.0.0"

#mode = "production"
mode = "development"

application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@127.0.0.1/for19' 

application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
application.config['SQLALCHEMY_POOL_SIZE'] = 50
application.config['SQLALCHEMY_MAX_OVERFLOW'] = 50
application.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False # No debug intercepts


login_manager = flask_login.LoginManager()
login_manager.init_app(application)
login_manager.session_protection = None


with application.app_context():
    db.init_app(application)
    db.create_all()

@application.route("/", methods=['POST', 'GET'])
def home():
    return flask.render_template('home.html')

@application.route("/methodology")
def methodology():
    return flask.render_template("methodology.html")

@application.route("/carbon_app", methods=['POST', 'GET'])
def carbon_application():
    return flask.render_template("carbon_app.html")

#Login/User managment

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == user_id).first()

@application.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        data = request.form
        print(f"Username: {data['email']}")
        print(f"Password: {data['password']}")

        if User.valid_login(data["email"], data["password"]) != None:    
            flask_login.login_user(User.valid_login(data["email"], data["password"]))
            flash("Congratz, your login was successful!")
            flash(f'Welcome to our carbone app {flask_login.current_user.username}')
            session['logged_in'] = True
            return flask.redirect("/")
        else:
            flash("Login failed. Please enter correct email and password.")
            return flask.redirect('/login')
    else:
        return flask.render_template('login.html')

@application.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        data = request.form
        new_user = User((data["f:name"] +" " + data["l:name"]), data['email'], data['password'])
        db.session.add(new_user)
        db.session.commit()
        flask_login.login_user(User.valid_login(data["email"], data["password"]))
        flash("Congratz, your registration was successful!")
        flash(f'Welcome to our carbone app {flask_login.current_user.username}')
        session['logged_in'] = True
        return flask.redirect("/")
    return flask.render_template('register.html')

@application.route("/logout",  methods=['POST', 'GET'])
def logout():
    flask_login.logout_user()
    session.clear()
    flash("You are loged out!")
    return flask.redirect("/")

@application.errorhandler(404)
def error(e):
    return flask.render_template('404.html') 

if __name__ == "__main__":
    if mode == "production":
        application.run(port=PRO_HOST, host=DEV_HOST)
    else:
        application.run(port=DEV_PORT, host=DEV_HOST, debug=True)
