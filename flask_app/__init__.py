from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = "shhhhh"

    from flask_app.controllers import app2

    return app
