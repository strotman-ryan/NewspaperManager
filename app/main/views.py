#main.views.py

from flask import render_template, session, redirect, url_for, flash

from . import main
from ..models import AccessDataBase
from . import forms

@main.route('/')
def index():
    return render_template('index.html', addcustomerlink = url_for('.customers'))

@main.route('/customers/add', methods=['GET','POST'])
def addcustomer():
    form = forms.AddCustomer()
    if form.validate_on_submit():
        session["address"] = form.address.data
        session["last_name"] = form.last_name.data
        AccessDataBase.addCustomer(form.last_name.data, form.address.data)
        form.address.data = None
        form.last_name.data = None
        return redirect(url_for('.addcustomer'))
    return render_template('addcustomer.html',form = form, address = session.get("address"), name = session.get("last_name"))

@main.route('/customers')
def customers():
    customers = AccessDataBase.getallcustomers()   
    return render_template('customers.html', customers = customers, link_str = ".editcustomer", add_cust_link = url_for(".addcustomer"))

@main.route('/customers/edit/<id>', methods=['GET','POST'])
def editcustomer(id):
    customer = AccessDataBase.getCustomer(id)
    return render_template('customer_edit.html', customer = customer)

