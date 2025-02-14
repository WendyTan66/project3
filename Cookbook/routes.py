from flask import render_template, request,redirect,url_for
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
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")