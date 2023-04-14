from . import APIKEY, COINS
from config import DEFAULT_PAG, PAG_SIZE
import sqlite3
import requests

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

    def balance(self):
        conexion = sqlite3.connect(self.route)
        cursor = conexion.cursor()

        moves_in = {}
        moves_out = {}
        moves = [moves_in, moves_out]

        sql_calls = ["SELECT SUM(from_quantity) FROM movements WHERE from_currency=?",
                     "SELECT SUM(to_quantity) FROM movements WHERE to_currency =?"]
        index = 0
        for call in sql_calls:
            for coin in COINS:
                cursor.execute(call, (coin[0],))
                data = cursor.fetchone()
                move = moves[index]
                if data[0]:
                    move[coin[0]] = data[0]
            index += 1

        crypto_balance = {}
        eur_balance = moves_out.get('EUR') - moves_in.get('EUR')

        for key in moves_out:
            if key != 'EUR':
                try:
                    balance = moves_out.get(key) - moves_in.get(key)

                except:
                    balance = moves_out.get(key)
                crypto_balance[key] = balance

        url = 'https://rest.coinapi.io/v1/exchangerate/EUR?invert=false'
        headers = {'X-CoinAPI-Key': APIKEY}
        response = requests.get(url, headers=headers)
        data = response.json()
        data_rates = data['rates']

        actual_crypto_value = {}
        i = 0

        while i < len(data_rates):
            for crypto in crypto_balance.keys():
                if data_rates[i]['asset_id_quote'] == crypto:

                    actual_exchante_rate = data_rates[i]['rate']
                    wallet_amount = crypto_balance[crypto]

                    actual_value = wallet_amount/actual_exchante_rate

                    actual_crypto_value[crypto] = actual_value
            i += 1

        actual_wallet_amount = 0
        for value in actual_crypto_value.values():
            actual_wallet_amount += value

        all_data = {
            "total_invested": moves_in,
            "total_withdrawed": moves_out,
            "total_euros_invested": moves_in.get('EUR'),
            "euro_balance": eur_balance,
            "crypto_balance": crypto_balance,
            "valores_actuales_de_mis_cripto": actual_crypto_value,
            "euro_wallet_amount": actual_wallet_amount
        }
        return all_data
