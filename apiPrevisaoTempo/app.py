from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = 'COLOCAR_KEY'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/weather")
def weather():
    city = request.args.get("city")

    if not city:
        return jsonify({"error": "Cidade não informada!"})

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=pt"

    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        return jsonify({"error": "Cidade não encontrada!"})

    return jsonify({
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"]
    })

if __name__ == "__main__":
    app.run(debug=True)





