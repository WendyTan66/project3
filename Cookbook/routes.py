from flask import render_template
from Cookbook import app,db
from Cookbook.models import Category, Recipe


@app.route("/")
def home():
    return render_template("cookbook.html")


@app.route("/categories")
def categories():
    return render_template("categories.html")

@app.route("/add_category", methods=["GET","POST"])
def add_category():
    return render_template("add_category.html")