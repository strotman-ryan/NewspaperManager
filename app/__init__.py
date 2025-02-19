
from flask import Flask, Blueprint

from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()
bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    bootstrap.init_app(app)
    db.init_app(app)
    return(app)