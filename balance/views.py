from flask import render_template
from . import app
from .forms import MovementForm

ROUTE = app.config.get('ROUTE')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/purchase')
def purchase():
    formulary = MovementForm()
    return render_template('purchase.html', form=formulary)


@app.route('/status')
def status():
    return render_template('status.html')
