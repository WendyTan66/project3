from flask import render_template, request, redirect, url_for
from Cookbook import app,db
from Cookbook.models import Category, Recipe


@app.route("/")
def home():
    recipes = list(Recipe.query.order_by(Recipe.id).all())
    return render_template("cookbook.html", recipes=recipes)


@app.route("/categories")
def categories():
    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=categories)

@app.route("/add_category", methods=["GET","POST"])
def add_category():
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")



@app.route("/edit_category/<int:category_id>", methods=["GET","POST"])
def edit_category(category_id):
    category=Category.query.get_or_404(category_id)
    if request.method == "POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_category.html",category=category)


@app.route("/delete_category/<int:category_id>")
def delete_category(category_id):
    category=Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for("categories"))


@app.route("/share_recipe", methods=["GET","POST"])
def share_recipe():
    categories = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        recipe = Recipe(
            title=request.form.get("title"),
            ingredients=request.form.get("ingredients"),
            instructions=request.form.get("instructions"),
            category_id=request.form.get("category_id")
        )
        db.session.add(recipe)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("share_recipe.html", categories=categories)


@app.route("/edit_recipe/<int:recipe_id>", methods=["GET","POST"])
def edit_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    categories = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        recipe.title = request.form.get("title"),
        recipe.ingredients=request.form.get("ingredients"),
        recipe.instructions=request.form.get("instructions"),
        recipe.category_id=request.form.get("category_id")
        db.session.commit()
    
    return render_template("edit_recipe.html", recipe=recipe, categories=categories)

@app.route("/delete_recipe/<int:recipe_id>")
def delete_recipe(recipe_id):
    recipe=Recipe.query.get_or_404(recipe_id)
    db.session.delete(recipe)
    db.session.commit()
    return redirect(url_for("home"))