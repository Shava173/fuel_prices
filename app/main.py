import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from flask import render_template
import requests
from app import app

@app.route('/')
def index():
    # Приклад отримання даних з ExchangeRate-API
    api_key = "bbfc46abece73ae8d6699e3f"
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
    response = requests.get(url).json()

    usd_to_eur = response.get('conversion_rates').get('EUR')
    usd_to_gbp = response.get('conversion_rates').get('GBP')
    usd_to_jpy = response.get('conversion_rates').get('JPY')

    return render_template('index.html', eur=usd_to_eur, gbp=usd_to_gbp, jpy=usd_to_jpy)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
