from .config import *

from App.models.test_model import *
from .restful_urls import *
from .exts import init_exts

from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    init_exts(app)

    return app
