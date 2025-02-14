from Cookbook import db

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    recipes = db.relationship('Recipe', backref='category', cascade="all,delete", lazy=True)
    def __repr__(self):
        #represent itself in the form of a string
        return self.category_name

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id', ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        #__repr__to represent itself in the form of a string
        return f"<Recipe {self.title}>"
