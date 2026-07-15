import os
import logging
from dotenv import load_dotenv

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_login import LoginManager
from werkzeug.middleware.proxy_fix import ProxyFix

# Load environment variables from .env file (for local development)
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.DEBUG)

class Base(DeclarativeBase):
    pass

# Initialize extensions
db = SQLAlchemy(model_class=Base)
login_manager = LoginManager()

# Create the app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET")

# Validate SESSION_SECRET is set
if not app.secret_key:
    if os.environ.get("FLASK_ENV") == "production":
        raise ValueError(
            "SESSION_SECRET environment variable is required in production. "
            "Please set it in your Render environment variables."
        )
    else:
        # Development fallback
        app.secret_key = "dev-secret-key-change-in-production"
        logging.warning("⚠️ Using development secret key. Set SESSION_SECRET for production.")

app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

# Configure database
# For Render: Use PostgreSQL via DATABASE_URL environment variable
# For local development: Falls back to SQLite in current directory
database_url = os.environ.get("DATABASE_URL")

if database_url:
    # Production database (PostgreSQL on Render)
    # Fix SQLAlchemy 2.0 compatibility for postgresql URLs
    if database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = database_url
else:
    # Local development database (SQLite)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///lost_and_found.db"
    logging.warning("⚠️ Using local SQLite database. For production, set DATABASE_URL environment variable.")

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}

# Initialize the app with extensions
db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

with app.app_context():
    # Import models here to avoid circular imports
    from models import User, LostItem, FoundItem, Match, ItemCategory
    from utils import create_default_categories

    # Create all database tables
    db.create_all()

    # Create default categories
    create_default_categories()

import app_routes
