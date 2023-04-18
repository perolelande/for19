from flask import render_template, Blueprint, request, redirect, url_for, flash
from app.models import Transport
from app import db
from datetime import timedelta, datetime
from flask_login import login_required, current_user
from app.carbon_app.forms import BusForm, CarForm, PlaneForm, FerryForm, MotorbikeForm, BicycleForm, WalkForm
import flask

carbon_app=Blueprint('carbon_app',__name__)

@carbon_app.route("/carbon_app")
def carbon_application():
    return render_template("carbon_app.html")

@carbon_app.route("/my_data")
def my_data():
    return render_template("my_data.html")
  