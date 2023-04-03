from flask_wtf import FlaskForm
from wtforms import DateField, FloatField, IntegerField, RadioField, StringField, SubmitField, SelectField
from wtforms.widgets import HiddenInput
from wtforms.validators import DataRequired
import datetime
from . import COINS


class MovementForm(FlaskForm):
    format_date = datetime.datetime.now().date()
    format_time = datetime.datetime.now().date().strftime('%H:%M:%S.%f')[:-3]

    id = IntegerField(default=0, widget=HiddenInput())
    date = DateField(default=format_date,
                     widget=HiddenInput)
    time = DateField(default=format_time,
                     widget=HiddenInput)

    from_currency = SelectField(
        'Currency', choices=COINS, validate_choice=True)
    from_quantity = FloatField('Quantity', validators=[DataRequired(
        message="You must introduce a number")])
    to_currency = SelectField(
        'Currency', choices=COINS, validate_choice=True)

    to_quantity = FloatField()
    u_price = FloatField()

    submit = SubmitField('Submit')
