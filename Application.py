#Flask application for megan

from flask import Flask, render_template, session, redirect, url_for, flash
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import os

application = app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY']  = "j;LJD:OSIFjFDFP(*Y(PSPA*Y))"
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
print('sqlite:///' + os.path.join(basedir, 'DataBase.sqlite'))

@app.route('/')
def index():
    return "hello world" # render_template('index.html')

@app.route('/customers/add', methods=['GET','POST'])
def addcustomer():
    form = AddCustomer()
    if form.validate_on_submit():
        session["address"] = form.address.data
        flash("Good adding")
        session["last_name"] = form.last_name.data
        form.address.data = None
        form.last_name.data = None
        return redirect(url_for('addcustomer'))
    return render_template('addcustomer.html',form = form, address = session.get("address"), name = session.get("last_name"))


class AddCustomer(FlaskForm):
    last_name = StringField("Family Name:", validators=[DataRequired()])
    address = StringField("Address:", validators=[DataRequired()])
    submit = SubmitField("Add")

if __name__ == '__main__':
    app.run(debug = True)

