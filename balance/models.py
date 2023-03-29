from . import APIKEY

import requests

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
                f'Error {response.status_code} {response.reason} al consultar la API'
            )
