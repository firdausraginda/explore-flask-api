from flask import Flask, jsonify
import os
from src.auth import auth
from src.bookmarks import bookmarks
from src.database import db
from flask_jwt_extended import JWTManager


def create_app(test_config=None):
    
    app = Flask(__name__, 
        instance_relative_config=True) # __name__ to defined where it is being configured from

    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY = os.environ.get("SECRET_KEY"),
            SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DB_URI"),
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
            JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
        )
    else:
        app.config.from_mapping(test_config)
    
    @app.get("/")
    def index():
        return "hello world"

    @app.get("/hello")
    def say_hello():
        return jsonify({"message": "hello world"})

    db.app = app
    db.init_app(app)

    JWTManager(app)

    app.register_blueprint(auth)
    app.register_blueprint(bookmarks)
    
    return app