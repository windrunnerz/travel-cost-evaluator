# transportmittel: bus, bahn, auto, flugzeug, fahrrad, zu fuss, e-scooter

# _____________________________________________________________________________
class ReiseIO:
    """Nimmt Benutzereingaben an und gibt die Gesamtkosten aus"""

    # static method arbeitet unabhängig von einer Klasseninstanz, d.h. sie benötigt keinen Zugriff auf Instanzvariablen
    # (self) oder Klassenvariablen (cls). Die Methode verarbeitet nur Eingabedaten und gibt sie wieder zurück"""
    @staticmethod
    def standard_eingabe():
        # Standardabfrage für alle Transportmittel
        strecke = float(input("Gebe die Strecke in km ein: ").replace(',', '.'))
        reisezeit = float(input("Gebe die Reisezeit in Stunden ein: ").replace(',', '.'))
        return strecke, reisezeit
        # Fehler abfangen, wenn ',' anstatt '.' für Kommazahlen eingegeben wird
        # .lower wandelt Eingabe in Kleinbuchstaben um → für Validierung sinnvoll, da einheitlich

    @staticmethod
    def eingabe():
        # Transportmittel abfragen
        while True:
            transportmittel_input = input("Gebe das Transportmittel ein (nur Auto, Bus, Zug oder Fahrrad möglich!): ")\
                .lower()

            if transportmittel_input in ["auto", "bus", "zug", "fahrrad"]:
                break
            else:
                print("Transportmittel nur Auto, Bus, Zug oder Fahrrad möglich! Bitte erneut eingeben.")

        # Strecke und Reisezeit abfragen, wenn Transportmittel relevant
        strecke, reisezeit = None, None
        if transportmittel_input in ["auto", "bus", "zug"]:
            strecke, reisezeit = ReiseIO.standard_eingabe()
        elif transportmittel_input == "fahrrad":
            strecke = float(input("Gebe die Strecke in km ein: ").replace(',', '.'))

        # zusätzliche Eingaben basierend auf Transportmittel
        if transportmittel_input == "auto":
            spritkosten = float(input("Wie viel kostet 1L Sprit?(z.B. 1,74): ").replace(',', '.'))
            verbrauch = float(input("Wie viel verbraucht das Auto auf 100km?: ").replace(',', '.'))
            return {
                "transportmittel": transportmittel_input,
                "strecke": strecke,
                "reisezeit": reisezeit,
                "spritkosten": spritkosten,
                "verbrauch": verbrauch
            }

        elif transportmittel_input == "fahrrad":
            koerpergewicht = float(input("Gebe dein Körpergewicht in kg ein: ").replace(',', '.'))
            skill_level = int(
                input(f"Gebe dein Skill Level an (1, 2, 3): \n1: Dreirad\n2: Normal\n3: Triathlon-Profi\n"))
            return {
                "transportmittel": transportmittel_input,
                "strecke": strecke,
                "koerpergewicht": koerpergewicht,
                "skill_level": skill_level
            }

        elif transportmittel_input == "bus":
            ticketpreis = float(input("Wie viel kostet das Busticket in Euro?: "))
            return {
                "transportmittel": transportmittel_input,
                "strecke": strecke,
                "reisezeit": reisezeit,
                "ticketpreis": ticketpreis
            }

        elif transportmittel_input == "zug":
            ticketpreis = float(input("Wie viel kostet das Zugticket in Euro?: "))
            return {
                "transportmittel": transportmittel_input,
                "strecke": strecke,
                "reisezeit": reisezeit,
                "ticketpreis": ticketpreis
            }


if __name__ == "__main__":
    # Hauptprogramm
    reise_io = ReiseIO()
    benutzer_eingaben = ReiseIO.eingabe()

    transportmittel = None

    if benutzer_eingaben["transportmittel"] == "auto":
        transportmittel = Auto(strecke=benutzer_eingaben["strecke"],
                               reisezeit=benutzer_eingaben["reisezeit"],
                               spritkosten=benutzer_eingaben["spritkosten"],
                               verbrauch=benutzer_eingaben["verbrauch"])
    elif benutzer_eingaben["transportmittel"] == "fahrrad":
        transportmittel = Fahrrad(strecke=benutzer_eingaben["strecke"],
                                  koerpergewicht=benutzer_eingaben["koerpergewicht"],
                                  skill_level=benutzer_eingaben["skill_level"])
    elif benutzer_eingaben["transportmittel"] == "bus":
        transportmittel = Bus(strecke=benutzer_eingaben["strecke"],
                              reisezeit=benutzer_eingaben["reisezeit"],
                              ticketpreis=benutzer_eingaben["ticketpreis"])
    elif benutzer_eingaben["transportmittel"] == "zug":
        transportmittel = Zug(strecke=benutzer_eingaben["strecke"],
                              reisezeit=benutzer_eingaben["reisezeit"],
                              ticketpreis=benutzer_eingaben["ticketpreis"])

    # Polymorphe Ausgabe
    transportmittel.ausgabe_details()

    # Übergabe testen
    # auto1 = auto(strecke=100, reisezeit=25, spritkosten=1.63, verbrauch=4.8)
    # kosten = auto1.berechne_kosten()
