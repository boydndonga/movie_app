from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap
from . import error, views

app = Flask(__name__, instance_relative_config=True)

# Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')
bootstrap = Bootstrap(app)

