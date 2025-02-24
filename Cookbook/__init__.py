import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


if os.environ.get("DEVELOPMENT") == "True":
    # If in development mode, use the local database URL (DB_URL)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    # If in production mode, use the live database URL (DATABASE_URL)
    uri = os.environ.get("DATABASE_URL")
    if uri and uri.startswith("postgres://"):
        # If the URL uses the old postgres:// format, change it to postgresql://
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from Cookbook import routes
from Cookbook import models

from dotenv import load_dotenv
load_dotenv()

