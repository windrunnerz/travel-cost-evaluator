# transportmittel: bus, bahn, auto, flugzeug, fahrrad, zu fuss, e-scooter
from src import ReiseIO, create_transportmittel, cli_main


def main():
    benutzer_eingaben = ReiseIO.eingabe()
    transportmittel = create_transportmittel(benutzer_eingaben)
    transportmittel.ausgabe_details()


if __name__ == "__main__":
    cli_main()
