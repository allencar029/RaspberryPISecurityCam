from flask import Flask

app = Flask(__name__)
app.secret_key = "shhhhh"

from flask_app.controllers import app2
