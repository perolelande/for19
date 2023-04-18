from flask import render_template, Blueprint
import flask

methodology=Blueprint('methodology',__name__)

@methodology.route("/methodology")
def methodology_m():
    return render_template("methodology.html")