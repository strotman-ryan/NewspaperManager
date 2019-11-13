#Flask application for megan

from flask import Flask, render_template, session, redirect, url_for, flash, Blueprint

from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config
from app.main import main as main_blueprint


db = SQLAlchemy()
bootstrap = Bootstrap()
def create_app(config_name):
    app = Flask(__name__)
    app.register_blueprint(main_blueprint)
    app.config.from_object(config[config_name])
    
    config[config_name].init_app(app)
    bootstrap.init_app(app)
    #db.init_app(app)
    
    return(app)
    


    
application = app = create_app('default')

if __name__ == "__main__":
    app.run()

