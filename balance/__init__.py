from flask import Flask
from flask_cors import CORS

APIKEY = 'E6A881EC-A489-4A17-BD9D-354A4625D54A'
# APIKEY = 'A64FF26D-9DBE-472B-9AEA-BE1E93B6C932'
# APIKEY = '4AD6E075-1F3D-4CB0-8309-76741E5D4BA2'

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
