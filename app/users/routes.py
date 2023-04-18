from flask import render_template, Blueprint, redirect, flash, url_for, request
from app.users.forms import RegistrationForm, LoginForm
from app.models import User
from app import db, bcrypt
from flask_login import login_user, current_user, logout_user
import flask 

users=Blueprint('users',__name__)
@users.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        data = request.form
        print(f"Username: {data['email']}")
        print(f"Username: {data['password']}")

        if users.valid_login(data["email"], data["password"]):    
            flash(f'Your login was successful! Welcome to our Carbon App, {users.get_full_name(data["email"])}!')
            return flask.redirect("/")
        else:
            flash("Login failed. Please enter correct email and password.")
            return flask.redirect('login')
    return render_template('login.html')

@users.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        data = request.form
        print(f"First Name: {data['f:name']}")
        print(f"Last Name: {data['l:name']}")
        print(f"Email: {data['email']}")
        print(f"Password: {data['password']}")
        new_user = User(data["f:name"], data["l:name"], data['email'], data['password'])
        users.add(new_user)

    return render_template('register.html')

