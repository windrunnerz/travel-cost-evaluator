"""
Web-App-Modul: Flask API mit verschiedenen Frontend-Routen

Dieses Modul steuert die Kommunikation zwischen Frontend und Backend.
Die Route '/api/evaluate' nimmt JSON-Daten vom Frontend entgegen, extrahiert
alle relevanten Felder (abhängig vom gewählten Fahrzeugtyp) und übergibt nur 
die tatsächlich benötigten Parameter an den Service-Layer (services.py).

Design-Prinzip:
- Die Route entscheidet, welche Felder weitergegeben werden.
- Der Service-Layer (services.py) kümmert sich ausschließlich um die Berechnung und
  bleibt frei von unnötiger Request-Logik.

Zusätzliche Routen (z.B. '/api/history') können unabhängig von der Hauptberechnung
für weitere Funktionalitäten genutzt werden.
"""

from flask import Flask, render_template, request, jsonify# , current_app
from .services import berechne_reisekosten_service
from .utils import convert_snake_to_camel

app = Flask(__name__)
history_list = []


@app.route("/")
def home():
    """Render die Startseite mit dem Hauptformular."""
    return render_template("index.html")


@app.route("/api/evaluate", methods=["POST"])
def evaluate():
    """
    Empfängt JSON-Payload vom Frontend, ruft die Service-Berechnung auf
    und gibt die Ergebnisse als JSON-Response zurück.
    """
    data = request.json
    if data is None:
        return jsonify({"error": "Ungültige oder fehlende Werte."}), 400

    fahrzeug_typ = data.get("fahrzeug_typ")
    mitfahrer = data.get("mitfahrer_anzahl")
    strecke = data.get("strecke_km")
    reisezeit = data.get("reisezeit")
    verbrauch = data.get("verbrauch_l_pro_100km")
    spritkosten = data.get("spritkosten_pro_liter")
    koerpergewicht = data.get("koerpergewicht")
    skill_level = data.get("skill_level")
    ticket_preis = data.get("ticket_preis")

    result = berechne_reisekosten_service(
        fahrzeug_typ=fahrzeug_typ,
        strecke=strecke,
        reisezeit=reisezeit,
        verbrauch=verbrauch,
        spritkosten=spritkosten,
        mitfahrer=mitfahrer,
        koerpergewicht=koerpergewicht,
        skill_level=skill_level,
        ticket_preis=ticket_preis
    )

    history_list.append(result)
    camel_result = convert_snake_to_camel(result)
    return jsonify(camel_result)



@app.route("/api/history", methods=["GET"])
def show_history():
    """Zeigt eine Liste der Ergebnisse"""
    camel_history = [convert_snake_to_camel(entry) for entry in history_list]
    return jsonify(camel_history)


if __name__ == "__main__":
    app.run(debug=True)

@app.errorhandler(400)
def bad_request(e):
    return jsonify({"error": "Bad Request"}), 400

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Not Found"}), 404

@app.errorhandler(500)
def internal_error(e):
    app.logger.error(f"Interner Serverfehler: {e}", exc_info=True)
    return jsonify({"error": "Internal Server Error"}), 500
