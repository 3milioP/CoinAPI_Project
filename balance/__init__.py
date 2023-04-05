from flask import Flask
from flask_cors import CORS

APIKEY = 'E6A881EC-A489-4A17-BD9D-354A4625D54A'

COINS = [("EUR", "EUR - Euro"),
         ("USD", "USD - Dólar"),
         ("BTC", "BTC - Bitcoin"),
         ("ETH", "ETH - Ethereum"),
         ("BNB", "BNB - Binance coin"),
         ("ADA", "ADA - Cardano")]

app = Flask(__name__)
app.config.from_object('config')
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
