from flask import Flask, render_template
import requests

app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY = 'deploy',
    DEBUG = False
)

rockets_api = 'https://api.spacexdata.com/v4/rockets'
ships_api = 'https://api.spacexdata.com/v4/ships'

@app.route('/')
def index():

    rockets = requests.get(rockets_api)
    ships = requests.get(ships_api)

    rockets = rockets.json()
    ships = ships.json()

    return render_template(
        'index.html',
        rockets = rockets,
        ships=ships
    )