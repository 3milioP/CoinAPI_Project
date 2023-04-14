from . import COINS
from flask_wtf import FlaskForm
from wtforms import FloatField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired
from wtforms.widgets import HiddenInput

class MovementForm(FlaskForm):

    id = IntegerField(default=0, widget=HiddenInput())
    from_currency = SelectField(
        'Currency', choices=COINS)
    from_quantity = FloatField('Quantity', validators=[DataRequired(
        message="You must introduce a number")])

    to_currency = SelectField(
        'Currency', choices=COINS)

    to_quantity = FloatField('to_quantity', render_kw={'readonly': True})

    u_price = FloatField('Unitary Price', render_kw={'readonly': True})

    submit = SubmitField('Submit')
