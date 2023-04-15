from . import COINS
from flask_wtf import FlaskForm
from wtforms import FloatField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired
from wtforms.widgets import HiddenInput


class MovementForm(FlaskForm):

    id = IntegerField(default=0, widget=HiddenInput())
    from_currency = SelectField(
        'Choose', choices=COINS)
    from_quantity = FloatField('Type amount', validators=[DataRequired(
        message="You must introduce a number")])

    to_currency = SelectField(
        'To', choices=COINS)

    to_quantity = FloatField('Quantity', render_kw={'readonly': True})

    u_price = FloatField('Best rate right now', render_kw={'readonly': True})

    submit = SubmitField('Submit')
