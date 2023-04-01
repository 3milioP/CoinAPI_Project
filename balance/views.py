from .models import DBManager
from config import DEFAULT_PAG, PAG_SIZE
from flask import render_template
from . import app
from flask import jsonify, request

RUTA = app.config.get('RUTA')


# Llamadas a la API, devuelven JSON

# RUTA = app.config.get('RUTA')


# @app.route('/api/v1/movements')
# def list_movements():
#     try:

#         try:
#             pagina = int(request.args.get('p', DEFAULT_PAG))
#         except:
#             pagina = DEFAULT_PAG

#         try:
#             tamanyo = int(request.args.get('r', PAG_SIZE))
#         except:
#             tamanyo = PAG_SIZE

#         db = DBManager(RUTA)
#         sql = 'SELECT * FROM movements'
#         movements = db.consultSQL(sql, pagina, tamanyo)
#         if len(movements) > 0:
#             resultado = {
#                 "status": "success",
#                 "results": movements
#             }
#             status_code = 200
#         else:
#             resultado = {
#                 'status': 'error',
#                 'message': f'There are no movements in the system'
#             }
#             status_code = 404

#     except Exception as error:
#         resultado = {
#             "status": "error",
#             "message": str(error)
#         }
#         status_code = 500

#     return jsonify(resultado), status_code


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/purchase')
def purchase():
    return render_template('purchase.html')


@app.route('/status')
def status():
    return render_template('status.html')
