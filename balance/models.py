from . import APIKEY
from config import DEFAULT_PAG, PAG_SIZE

import requests
import sqlite3

api_url = 'http://rest-sandbox.coinapi.io'
endpoint = '/v1/exchangerate'
headers = {
    'X-CoinAPI-Key': APIKEY
}


class APIError(Exception):
    pass


class CriptoModel:
    orin = ''
    dest = ''

    def __init__(self):
        self.change = 0.0

    def consult_change(self):
        url = f'{api_url}{endpoint}/{self.orin}/{self.dest}'
        response = requests.get(url, headers)

        if response.status_code == 200:
            exchange = response.json()
            self.change = exchange.get("rate")
        else:
            raise APIError(
                f'Error {response.status_code} {response.reason} in API consult'
            )


class DBManager:
    def __init__(self, route):
        self.route = route

    def consultSQL(self, consult, pag=DEFAULT_PAG, nreg=PAG_SIZE):
        conexion = sqlite3.connect(self.route)
        offset = nreg*(pag - 1)
        consult = f'{consult} LIMIT {nreg} OFFSET {offset}'

        cursor = conexion.cursor()
        cursor.execute(consult)
        data = cursor.fetchall()

        self.movements = []
        col_names = []

        for col in cursor.description:
            col_names.append(col[0])

        for datum in data:
            index = 0
            movement = {}
            for name in col_names:
                movement[name] = datum[index]
                index += 1

            self.movements.append(movement)

        conexion.close()

        return self.movements

    def connect(self):
        conexion = sqlite3.connect(self.route)
        cursor = conexion.cursor()

        return conexion, cursor

    def disconnect(self, conexion):
        conexion.close()

    def consultWithParams(self, consult, params):
        conexion, cursor = self.connect()

        result = False
        try:
            cursor.execute(consult, params)
            conexion.commit()
            result = True
        except Exception as ex:
            print(ex)
            conexion.rollback()

        self.disconnect(conexion)
        return result

    def delete(self, id):
        consult = 'DELETE FROM movements WHERE id=?'
        conexion = sqlite3.connect(self.route)
        cursor = conexion.cursor()
        result = False
        try:
            cursor.execute(consult, (id,))
            conexion.commit()
            result = True
        except:
            conexion.rollback()

        conexion.close()
        return result

    def getMovement(self, id):

        consult = 'SELECT * FROM movements WHERE id=?'
        conexion = sqlite3.connect(self.route)
        cursor = conexion.cursor()
        cursor.execute(consult, (id,))

        data = cursor.fetchone()
        result = None

        if data:
            col_names = []
            for column in cursor.description:
                col_names.append(column[0])
            movement = {}
            index = 0
            for name in col_names:
                movement[name] = data[index]
                index += 1

            result = movement

        conexion.close()
        return result
