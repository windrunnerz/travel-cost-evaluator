VERBRAUCH_AUTO: float = 5   # L/km
SPRITKOSTEN_AUTO: float = 1.7   # €/L


def frage_transportmittel() -> dict:
    """
    Zentrale Eingabefunktion, die alles koordiniert.

    Returns:
        dict: Nutzereingaben aus Unterfunktionen
    """
    while True:
        transportmittel_input = input(
            "Gebe das Transportmittel ein (nur Auto, Bus, Zug oder Fahrrad möglich!): ").lower().strip()
        if transportmittel_input in ["auto", "bus", "zug", "fahrrad"]:
            break
        else:
            print("Transportmittel nur Auto, Bus, Zug oder Fahrrad möglich! Bitte erneut eingeben.")

    mapping = {
        "auto": _eingabe_auto,
        "fahrrad": _eingabe_fahrrad,
        "bus": lambda: _eingabe_hat_ticket("bus"),
        "zug": lambda: _eingabe_hat_ticket("zug")
    }

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


def _eingabe_auto() -> dict:
    strecke = frage_strecke()
    reisezeit = frage_reisezeit()
    spritkosten = SPRITKOSTEN_AUTO
    verbrauch = VERBRAUCH_AUTO
    return {
        "transportmittel": "auto",
        "strecke": strecke,
        "reisezeit": reisezeit,
        "spritkosten": spritkosten,
        "verbrauch": verbrauch
    }


def _eingabe_fahrrad() -> dict:
    strecke = frage_strecke()
    koerpergewicht = float(input("Gebe dein Körpergewicht in kg ein: ").replace(',', '.'))
    skill_level = int(input("Gebe dein Skill Level an (1, 2, 3): "))
    return {
        "transportmittel": "fahrrad",
        "strecke": strecke,
        "koerpergewicht": koerpergewicht,
        "skill_level": skill_level
    }


'''
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
'''


def _eingabe_hat_ticket(transportmittel: str) -> dict:
    """
    Für alle Transportmittel mit Ticket.

    Args:
        transportmittel (str): Das jeweilige Transportmittel (Bus, Zug, ...)

    Returns:
        dict: Alle relevanten Angaben für das Transportmittel
    """
    strecke = frage_strecke()
    reisezeit = frage_reisezeit()
    ticketpreis = float(input("Wie viel kostet das Ticket in Euro?: ").replace(',', '.'))
    return {
        "transportmittel": transportmittel,
        "strecke": strecke,
        "reisezeit": reisezeit,
        "ticketpreis": ticketpreis
    }
