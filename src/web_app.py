"""Web-App-Modul: Flask API mit verschiedenen Frontend-Routen"""

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
history_list = []


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/evaluate", methods=["POST"])
def evaluate():
    data = request.json

    try:
        strecke = data.get("strecke_km")
        verbrauch = data.get("verbrauch_l_pro_100km")
        kosten = data.get("kosten_pro_liter")
        mitfahrer = data.get("mitfahrer_anzahl")
    except (TypeError, ValueError):
        return jsonify({"error": "Ungültige oder fehlende Werte."}), 400

    gesamtkosten = (strecke / 100) * verbrauch * kosten

    if mitfahrer and mitfahrer > 0:
        kosten_pro_person = gesamtkosten / mitfahrer
    else:
        kosten_pro_person = gesamtkosten

    history_list.append({
        "strecke": strecke,
        "verbrauch": verbrauch,
        "kosten": kosten,
        "mitfahrer": mitfahrer,
        "gesamtkosten": gesamtkosten,
        "kosten_pro_person": kosten_pro_person
    })

    return jsonify({
        "gesamtkosten": round(gesamtkosten, 2),
        "kosten_pro_person": round(kosten_pro_person, 2)
    })


@app.route("/api/history", methods=["GET"])
def show_history():
    return jsonify(history_list)


if __name__ == "__main__":
    app.run(debug=True)
