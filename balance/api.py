from flask import jsonify, request

from . import app
from config import DEFAULT_PAG, PAG_SIZE

from .models import DBManager

# Llamadas a la API, devuelven JSON

RUTA = app.config.get('RUTA')


@app.route('/api/v1/movements')
def list_movements():
    try:

        try:
            pagina = int(request.args.get('p', DEFAULT_PAG))
        except:
            pagina = DEFAULT_PAG

        try:
            tamanyo = int(request.args.get('r', PAG_SIZE))
        except:
            tamanyo = PAG_SIZE

        db = DBManager(RUTA)
        sql = 'SELECT * FROM movements'
        movements = db.consultSQL(sql, pagina, tamanyo)
        if len(movements) > 0:
            resultado = {
                "status": "success",
                "results": movements
            }
            status_code = 200
        else:
            resultado = {
                'status': 'error',
                'message': f'There are no movements in the system'
            }
            status_code = 404

    except Exception as error:
        resultado = {
            "status": "error",
            "message": str(error)
        }
        status_code = 500

    return jsonify(resultado), status_code


@app.route('/api/v1/movimientos/<int:id>')
def get_movimiento(id):
    """
    instanciar DBManager
    preparar la consulta
    ejecutar la consulta
    leer el resultado
    si ok:
      resultado es success / movimiento
    si error:
      resultado es error / mensaje
    devolvemos el resultado
    """

    try:
        db = DBManager(RUTA)
        mov = db.obtenerMovimiento(id)
        if mov:
            resultado = {
                'status': 'success',
                'results': mov
            }
            status_code = 200
        else:
            resultado = {
                'status': 'error',
                'message': f'No he encontrado un movimiento con el ID={id}'
            }
            status_code = 404
    except Exception as error:
        resultado = {
            'status': 'error',
            'message': str(error)
        }
        status_code = 500

    return jsonify(resultado), status_code


@app.route('/api/v1/movements/<int:id>', methods=['DELETE'])
def delete_movements(id):

    try:
        db = DBManager(RUTA)
        mov = db.getMovement(id)
        if mov:
            sql = 'DELETE FROM movements WHERE id=?'
            is_deleted = db.consultWithParams(sql, (id,))
            if is_deleted:
                resultado = {
                    'status': 'success'
                }
                status_code = 204
            else:
                result = {
                    'status': 'error',
                    'message': f'The movement with ID={id} has not been deleted'
                }
                status_code = 500
        else:
            result = {
                'status': 'error',
                'message': f'There is no movement with ID={id} to delete'
            }
            status_code = 404
    except:
        result = {
            'status': 'error',
            'message': 'Unknown server error'
        }
        status_code = 500

    return jsonify(result), status_code


@app.route('/api/v1/movements', methods=['POST'])
def insert_movement():

    try:
        json = request.get_json()
        form = MovimientoForm(data=json)

        if form.validate():
            # si el formulario es válido
            db = DBManager(RUTA)
            # sql = 'INSERT INTO movimientos (fecha, concepto, tipo, cantidad) VALUES (?, ?, ?, ?)'
            # params = (form.fecha.data, form.concepto.data,
            #           form.tipo.data, form.cantidad.data)
            sql = 'INSERT INTO movements (fecha, concepto, tipo, cantidad) VALUES (:fecha, :concepto, :tipo, :cantidad)'
            params = request.json
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
                    'message': 'Could not insert movement'
                }
        else:
            # si el formulario tiene errores de validación
            status_code = 400
            result = {
                'status': 'error',
                'message': 'Invalid data recived',
                'errors': form.errors
            }

    except:
        status_code = 500
        result = {
            'status': 'error',
            'message': 'Unknown server error'
        }

    return jsonify(result), status_code


@app.route('/api/v1/movimientos/<int:id>', methods=['PUT'])
def modificar_movimiento(id):
    """
    200 - OK. La modificación se ha realizado
    400 - Si los datos recibidos no son válidos
    500 - Si hay error en el servidor
    """

    try:
        json = request.get_json()
        form = MovimientoForm(data=json)

        if form.validate():
            # El formulario es válido
            if id == form.id.data:
                db = DBManager(RUTA)
                sql = 'UPDATE movimientos SET fecha=?, concepto=?, tipo=?, cantidad=? WHERE id=?'
                params = (
                    form.fecha.data,
                    form.concepto.data,
                    form.tipo.data,
                    form.cantidad.data,
                    form.id.data
                )
                modificado = db.consultaConParametros(sql, params)
                if modificado:
                    status_code = 200
                    resultado = {
                        'status': 'success',
                        'results': form.data
                    }
                else:
                    status_code = 500
                    resultado = {
                        'status': 'error',
                        'message': 'No se ha podido insertar el movimiento'
                    }
            else:
                status_code = 400
                resultado = {
                    'status': 'error',
                    'message': 'Los datos enviados son inconsistentes'
                }
        else:
            status_code = 400
            resultado = {
                'status': 'error',
                'message': 'Los datos recibidos no son válidos',
                'errors': form.errors
            }

    except:
        status_code = 500
        resultado = {
            'status': 'error',
            'message': 'Error desconocido en el servidor'
        }
    return jsonify(resultado), status_code
