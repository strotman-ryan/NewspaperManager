#Flask application for megan

from flask import Flask, render_template
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap

application = app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY']  = "j;LJD:OSIFjFDFP(*Y(PSPA*Y))"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/customers/add', methods=['GET','POST'])
def addcustomer():
    address = None
    last_name = None
    form = AddCustomer()
    if form.validate_on_submit():
        address = form.address.data
        last_name = form.last_name.data
        form.address.data = None
        form.last_name.data = None
    return render_template('addcustomer.html',form = form, address = address, name = last_name)


class AddCustomer(FlaskForm):
    last_name = StringField("Family Name:", validators=[DataRequired()])
    address = StringField("Address:", validators=[DataRequired()])
    submit = SubmitField("Add")

if __name__ == '__main__':
    app.run(debug = True)

