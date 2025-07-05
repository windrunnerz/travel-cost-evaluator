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
        strecke = data.get("strecke_km") # type: ignore
        verbrauch = data.get("verbrauch_l_pro_100km") # type: ignore
        spritkosten = data.get("kosten_pro_liter") # type: ignore
        mitfahrer = data.get("mitfahrer_anzahl") # type: ignore
    except (TypeError, ValueError):
        return jsonify({"error": "Ungültige oder fehlende Werte."}), 400

    gesamtkosten = round((strecke / 100) * verbrauch * spritkosten, 2)

    if mitfahrer and mitfahrer > 0:
        kosten_pro_person = round(gesamtkosten / mitfahrer, 2)
    else:
        kosten_pro_person = gesamtkosten

    history_list.append({
        "strecke": strecke,
        "verbrauch": verbrauch,
        "spritkosten": spritkosten,
        "mitfahrer": mitfahrer,
        "gesamtkosten": gesamtkosten,
        "kosten_pro_person": kosten_pro_person
    })

    return jsonify({
        "gesamtkosten": gesamtkosten,
        "kosten_pro_person": kosten_pro_person
    })


@app.route("/api/history", methods=["GET"])
def show_history():
    return jsonify(history_list)


if __name__ == "__main__":
    app.run(debug=True)
