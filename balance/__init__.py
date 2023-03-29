from flask import Flask

APIKEY = 'E6A881EC-A489-4A17-BD9D-354A4625D54A'

app = Flask(__name__)
app.config.from_object('config')
