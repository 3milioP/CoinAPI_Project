from flask import Flask
from flask_cors import CORS

APIKEY = 'A64FF26D-9DBE-472B-9AEA-BE1E93B6C932'

COINS = [("EUR", "EUR - Euro"),
         ("BTC", "BTC - Bitcoin"),
         ("ETH", "ETH - Ethereum"),
         ("USDT", "USDT - Tether"),
         ("ADA", "ADA - Cardano"),
         ("SOL", "SOL - Solana"),
         ("XRP", "XRP - Ripple"),
         ("DOT", "DOT - Polkadot"),
         ("DOGE", "DOGE - Dogecoin"),
         ("SHIB", "SHIB - Shiba Inu")
         ]

app = Flask(__name__)
app.config.from_object('config')
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
