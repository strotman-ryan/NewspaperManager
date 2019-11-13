#main.views.py

from flask import render_template, session, redirect, url_for, flash
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from . import main

@main.route('/')
def index():
    return render_template('index.html', addcustomerlink = url_for('.addcustomer'))

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