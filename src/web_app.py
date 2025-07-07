"""Web-App-Modul: Flask API mit verschiedenen Frontend-Routen"""

from flask import Flask, render_template, request, jsonify
from .services import berechne_reisekosten_service

app = Flask(__name__)
history_list = []


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/evaluate", methods=["POST"])
def evaluate():
    data = request.json
    if data is None:
        return jsonify({"error": "Ungültige oder fehlende Werte."}), 400

    strecke = data.get("strecke_km")
    reisezeit = data.get("reisezeit")
    verbrauch = data.get("verbrauch_l_pro_100km")
    spritkosten = data.get("spritkosten_pro_liter")
    mitfahrer = data.get("mitfahrer_anzahl")
    fahrzeug_typ = data.get("fahrzeug_typ")
       
    result = berechne_reisekosten_service(
        fahrzeug_typ,
        strecke,
        reisezeit,
        verbrauch,
        spritkosten,
        mitfahrer
    )

    return jsonify(result)


@app.route("/api/history", methods=["GET"])
def show_history():
    return jsonify(history_list)


if __name__ == "__main__":
    app.run(debug=True)
