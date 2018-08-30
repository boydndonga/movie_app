from flask import Flask
from .config import DevConfig

app = Flask(__name__)

# Setting up configuration
app.config.from_object(DevConfig)

from . import error, views