#Flask application for megan

from flask import Flask, render_template, session, redirect, url_for, flash, Blueprint
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config


main = Blueprint('main', __name__)
db = SQLAlchemy()
bootstrap = Bootstrap()
def create_app(config_name):
    app = Flask(__name__)
    app.register_blueprint(main)
    app.config.from_object(config[config_name])
    
    config[config_name].init_app(app)
    bootstrap.init_app(app)
    #db.init_app(app)
    
    return(app)
    

@main.route('/')
def index():
    return "hello world" # render_template('index.html')

@main.route('/customers/add', methods=['GET','POST'])
def addcustomer():
    form = AddCustomer()
    if form.validate_on_submit():
        session["address"] = form.address.data
        flash("Good adding")
        session["last_name"] = form.last_name.data
        form.address.data = None
        form.last_name.data = None
        return redirect(url_for('.addcustomer'))
    return render_template('addcustomer.html',form = form, address = session.get("address"), name = session.get("last_name"))


class AddCustomer(FlaskForm):
    last_name = StringField("Family Name:", validators=[DataRequired()])
    address = StringField("Address:", validators=[DataRequired()])
    submit = SubmitField("Add")
    
application = app = create_app('default')

if __name__ == "__main__":
    app.run()

