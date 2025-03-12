def frage_transportmittel():
    while True:
        transportmittel_input = input(
            "Gebe das Transportmittel ein (nur Auto, Bus, Zug oder Fahrrad möglich!): ").lower().strip()
        if transportmittel_input in ["auto", "bus", "zug", "fahrrad"]:
            break
        else:
            print("Transportmittel nur Auto, Bus, Zug oder Fahrrad möglich! Bitte erneut eingeben.")

    # Mapping: Verknüpfe den Input mit der entsprechenden Eingabefunktion
    mapping = {
        "auto": eingabe_auto,
        "fahrrad": eingabe_fahrrad,
        "bus": eingabe_bus,
        "zug": eingabe_zug
    }

    # Rufe die entsprechende Funktion auf
    return mapping[transportmittel_input]()


def get_float_input(prompt: str) -> float:
    """
    Fragt den Benutzer nach einer Gleitkommazahl und validiert die Eingabe.

    Args:
        prompt (str): Die Eingabeaufforderung, die dem Benutzer angezeigt wird.

    Returns:
        float: Der gültige, in einen Float konvertierte Wert.
    """
    while True:
        user_input = input(prompt)
        try:
            value = float(user_input.replace(',', '.'))
            return value
        except ValueError:
            print("Ungültige Eingabe! Bitte eine Zahl eingeben.")


def frage_strecke() -> float:
    return get_float_input("Gebe die Strecke in km ein: ")


def frage_reisezeit() -> float:
    return get_float_input("Gebe die Reisezeit in Stunden ein: ")


def eingabe_auto():
    strecke = frage_strecke()
    reisezeit = frage_reisezeit()
    spritkosten = float(input("Wie viel kostet 1L Sprit? (z.B. 1,74): ").replace(',', '.'))
    verbrauch = float(input("Wie viel verbraucht das Auto auf 100km?: ").replace(',', '.'))
    return {
        "transportmittel": "auto",
        "strecke": strecke,
        "reisezeit": reisezeit,
        "spritkosten": spritkosten,
        "verbrauch": verbrauch
    }


def eingabe_fahrrad():
    strecke = frage_strecke()
    koerpergewicht = float(input("Gebe dein Körpergewicht in kg ein: ").replace(',', '.'))
    skill_level = int(input("Gebe dein Skill Level an (1, 2, 3): "))
    return {
        "transportmittel": "fahrrad",
        "strecke": strecke,
        "koerpergewicht": koerpergewicht,
        "skill_level": skill_level
    }


def eingabe_bus():
    strecke = frage_strecke()
    reisezeit = frage_reisezeit()
    ticketpreis = float(input("Wie viel kostet das Busticket in Euro?: ").replace(',', '.'))
    return {
        "transportmittel": "bus",
        "strecke": strecke,
        "reisezeit": reisezeit,
        "ticketpreis": ticketpreis
    }


def eingabe_zug():
    strecke = frage_strecke()
    reisezeit = frage_reisezeit()
    ticketpreis = float(input("Wie viel kostet das Zugticket in Euro?: ").replace(',', '.'))
    return {
        "transportmittel": "zug",
        "strecke": strecke,
        "reisezeit": reisezeit,
        "ticketpreis": ticketpreis
    }
