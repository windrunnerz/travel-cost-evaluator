# transportmittel: bus, bahn, auto, flugzeug, fahrrad, zu fuss, e-scooter
from src import ReiseIO, transportmittel_factory

if __name__ == "__main__":
    benutzer_eingaben = ReiseIO.eingabe()
    transportmittel = transportmittel_factory(benutzer_eingaben)
    transportmittel.ausgabe_details()
