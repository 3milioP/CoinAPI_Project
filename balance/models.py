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
        crypto_value = 0
        moves_in = {}
        moves_out = {}
        crypto_balance = {}
        actual_crypto_value = {}
        moves = [moves_in, moves_out]

        sql_calls = ["SELECT SUM(from_quantity) FROM movements WHERE from_currency=?",
                     "SELECT SUM(to_quantity) FROM movements WHERE to_currency =?"]
        # --------------- DATABASE CALL------------------
        index = 0
        for call in sql_calls:
            for coin in COINS:

                cursor.execute(call, (coin[0],))
                data = cursor.fetchone()
                move = moves[index]

                if data[0] != None:
                    move[coin[0]] = data[0]
            index += 1
        conexion.close()

        if moves_in.get('EUR') != None:
            try:
                eur_balance = moves_out.get('EUR') - moves_in.get('EUR')
            except TypeError:
                eur_balance = -moves_in.get('EUR')
        else:
            eur_balance = 0

        for key in moves_out:
            if key != 'EUR':
                try:
                    balance = moves_out.get(key) - moves_in.get(key)
                except TypeError:
                    balance = moves_out.get(key)

                crypto_balance[key] = balance
        # ------------- COINAPI CALL -----------------
        url = 'https://rest.coinapi.io/v1/exchangerate/EUR?invert=false'
        headers = {'X-CoinAPI-Key': APIKEY}
        response = requests.get(url, headers=headers)
        data = response.json()

        data_rates = data['rates']
        cryptos = crypto_balance.keys()

        i = 0

        while i < len(data_rates):
            for crypto in cryptos:
                if data_rates[i]['asset_id_quote'] == crypto:

                    actual_exchange_rate = data_rates[i]['rate']
                    wallet_amount = crypto_balance[crypto]

                    actual_value = wallet_amount/actual_exchange_rate

                    actual_crypto_value[crypto] = actual_value
            i += 1

        for value in actual_crypto_value.values():
            crypto_value += value

        total_euros_invested = moves_in.get('EUR')
        if total_euros_invested == None:
            total_euros_invested = 0

        actual_wallet_value = total_euros_invested + eur_balance + crypto_value

        all_data = {
            "total_euros_invested": total_euros_invested,
            "crypto_balance": crypto_balance,
            "cryptos": list(cryptos),
            "euro_wallet_amount": actual_wallet_value,
            "withdrawed": moves_out.get('EUR')
        }
        return all_data
