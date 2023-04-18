from flask import render_template, Blueprint
from app.models import User, Transport
import flask
home=Blueprint('home',__name__)

@home.route("/", methods=['POST', 'GET'])
def home_home():
    return render_template('home.html')