from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
API_KEY = 'your_openweathermap_api_key'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City is required'}), 400
    response = requests.get(BASE_URL, params={'q': city, 'appid': API_KEY, 'units': 'metric'})
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
