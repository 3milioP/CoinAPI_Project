from flask import Flask
from flask_cors import CORS

APIKEY = 'E6A881EC-A489-4A17-BD9D-354A4625D54A'

app = Flask(__name__)
app.config.from_object('config')
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
