from src import ReiseIO, create_transportmittel


def cli_main():
    benutzer_eingaben = ReiseIO.eingabe()
    transportmittel = create_transportmittel(benutzer_eingaben)
    transportmittel.ausgabe_details()


if __name__ == "__main__":
    cli_main()
