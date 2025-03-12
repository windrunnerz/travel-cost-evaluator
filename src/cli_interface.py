from .eingaben_reise import frage_transportmittel
from .transportmittel_factory import create_transportmittel


def cli_main():
    benutzer_eingaben = frage_transportmittel()
    transportmittel = create_transportmittel(benutzer_eingaben)
    transportmittel.ausgabe_details()


if __name__ == "__main__":
    cli_main()
