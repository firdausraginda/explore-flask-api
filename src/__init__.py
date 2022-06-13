from flask import Flask, jsonify

def create_app(test_config=None):
    
    app = Flask(__name__, 
        instance_relative_config=True) # __name__ to defined where it is being configured from

    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY="dev"
        )
    else:
        app.config.from_mapping(test_config)
    
    @app.get("/")
    def index():
        return "hello world"

    @app.get("/hello")
    def say_hello():
        return jsonify({"message": "hello world"})

    
    return app