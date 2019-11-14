#forms
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


class AddCustomer(FlaskForm):
    last_name = StringField("Family Name:", validators=[DataRequired()])
    address = StringField("Address:", validators=[DataRequired()])
    submit = SubmitField("Add")