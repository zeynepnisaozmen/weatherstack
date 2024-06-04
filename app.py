from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# weatherstack API
API_KEY = '8620c1a767b55fd476ebc688a337e00b'

# Hava durumu bilgilerini getiren yardımcı fonksiyon
def get_weather(city):
    url = f"http://api.weatherstack.com/current?access_key={API_KEY}&query={city}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Ana sayfa route'u
@app.route('/')
def home():
    return "Welcome to the Weather API!"

# Belirli bir şehrin hava durumunu getiren route
@app.route('/weather', methods=['GET'])
def weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "Please provide a city"}), 400

    weather_data = get_weather(city)
    if weather_data:
        return jsonify(weather_data)
    else:
        return jsonify({"error": "Unable to fetch weather data"}), 500

if __name__ == '__main__':
    app.run(debug=True)
