from flask import jsonify, request
import datetime
from . import app
from config import DEFAULT_PAG, PAG_SIZE
from .forms import MovementForm
from .models import DBManager

ROUTE = app.config.get('ROUTE')


@app.route('/api/v1/movements')
def list_movements():
    try:

        try:
            page = int(request.args.get('p', DEFAULT_PAG))
        except:
            page = DEFAULT_PAG

        try:
            size = int(request.args.get('r', PAG_SIZE))
        except:
            size = PAG_SIZE

        db = DBManager(ROUTE)
        sql = 'SELECT * FROM movements'
        movements = db.consultSQL(sql, page, size)
        if len(movements) > 0:
            result = {
                "status": "success",
                "results": movements
            }
            status_code = 200
        else:
            result = {
                'status': 'error',
                'message': f'There are no movements in the system'
            }
            status_code = 404

    except Exception as error:
        result = {
            "status": "error",
            "message": str(error)
        }
        status_code = 500

    return jsonify(result), status_code


@app.route('/api/v1/movements', methods=['POST'])
def insert_movement():

    json = request.get_json()
    form = MovementForm(data=json)
    try:
        json = request.get_json()
        form = MovementForm(data=json)

        if form.validate():

            db = DBManager(ROUTE)
            sql = 'INSERT INTO movements (date, time, from_currency, from_quantity, to_currency, to_quantity) VALUES (:date, :time, :from_currency, :from_quantity, :to_currency, :to_quantity)'
            params = request.json

            format_date = datetime.datetime.now().date()
            format_time = datetime.datetime.now(
            ).time().strftime('%H:%M:%S.%f')[:-3]
            params['date'] = format_date
            params['time'] = format_time

            isSuccess = db.consultWithParams(sql, params)
            if isSuccess:
                status_code = 201
                result = {
                    'status': 'success',
                }
            else:
                status_code = 500
                result = {
                    'status': 'error',
                    'message': "Couldn't insert the movement"
                }
        else:
            status_code = 400
            result = {
                'status': 'error',
                'message': 'Data recived not valid',
                'errors': form.errors
            }

    except:
        status_code = 500
        result = {
            'status': 'error',
            'message': 'Server unknown error'
        }

    return jsonify(result), status_code


@app.route('/api/v1/movements/data')
def get_balance():
    db = DBManager(ROUTE)
    data = db.balance()

    return jsonify(data)
