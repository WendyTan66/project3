from flask import render_template
from Cookbook import app,db
from Cookbook.models import User, Recipe

@app.route("/")
def home():
    return render_template("cookbook.html")
