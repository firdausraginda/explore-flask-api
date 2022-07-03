from flask import Flask, jsonify, redirect
import os
from src.auth import auth
from src.bookmarks import bookmarks
from src.constants.http_status_code import HTTP_404_NOT_FOUND
from src.database import db, Bookmark
from flask_jwt_extended import JWTManager
from flasgger import Swagger
from src.config.swagger import template, swagger_config


def create_app(test_config=None):
    
    app = Flask(__name__, 
        instance_relative_config=True) # __name__ to defined where it is being configured from

    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY = os.environ.get("SECRET_KEY"),
            SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DB_URI"),
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
            JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY"),
            SWAGGER = {
                'title': 'Bookmarks API',
                'uiversion': 3
            }
        )
    else:
        app.config.from_mapping(test_config)
    
    # @app.get("/")
    # def index():
    #     return "hello world"

    @app.get("/hello")
    def say_hello():
        return jsonify({"message": "hello world"})

    db.app = app
    db.init_app(app)

    JWTManager(app)

    app.register_blueprint(auth)
    app.register_blueprint(bookmarks)

    Swagger(app, config=swagger_config, template=template)

    @app.get('/<short_url>')
    def redirect_to_url(short_url):
        bookmark = Bookmark.query.filter_by(short_url=short_url).first_or_404()

        if bookmark:
            bookmark.visits = bookmark.visits + 1
            db.session.commit()

            return redirect(bookmark.url)
    
    @app.errorhandler(HTTP_404_NOT_FOUND)
    def handle_404(e):
        return jsonify({
            'message': f'{e}'
        }), HTTP_404_NOT_FOUND

    return app