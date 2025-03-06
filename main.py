# transportmittel: bus, bahn, auto, flugzeug, fahrrad, zu fuss, e-scooter
from abc import ABC, abstractmethod


# Oberklasse
class Transportmittel(ABC):
    """Berechnet Reisekosten für verschiedene Transportmittel"""

    def __init__(self, strecke, reisezeit):
        self.strecke = strecke
        self.reisezeit = reisezeit

    # Platzhalter, abstrakte Methode die signalisiert, dass jede Unterklasse ihre eigene Implementierung dieser
    # Methode bereitstellen muss. NotImplementedError ist eine eingebaute Exception-Klasse in Python → signalisiert
    # Fehlerzustände
    @abstractmethod
    def berechne_kosten(self):
        raise NotImplementedError("Diese Methode muss in der Unterklasse implementiert werden.")

    @abstractmethod
    def ausgabe_details(self):
        pass
    # @abstractmethod zeigt an, dass jede Unterklasse diese Methode implementieren muss


# Unterklasse Auto
class Auto(Transportmittel):
    def __init__(self, strecke, reisezeit, spritkosten, verbrauch):
        super().__init__(strecke, reisezeit)
        self.spritkosten = spritkosten
        self.verbrauch = verbrauch
        # super() ruft den Konstruktor der Oberklasse auf, 'strecke' und 'reisezeit' werden korrekt initialisiert und
        # stehen der Unterklasse zur Verfügung"""
        # Zuweisung der Parameter zu dem Attribut der Klasse auto. Der Wert von spritkosten wird in das Attribut
        # self.spritkosten gespeichert. Durch das Präfix self. wird das Attribut dem aktuellen Objekt der Klasse
        # zugeordnet

    def berechne_kosten(self):
        return (self.strecke / 100) * self.verbrauch * self.spritkosten
        # Rückgabewert, damit das Ergebnis der Kostenberechnung außerhalb der Funktion/Klasse verwendet werden kann

    def ausgabe_details(self):
        kosten = self.berechne_kosten()
        print(f"Das Auto fährt {self.strecke} km in {self.reisezeit} Stunden.")
        print(f"Die Gesamtkosten betragen: {kosten: .2f} Euro.")


# Unterklasse Fahrrad
class Fahrrad(Transportmittel):
    def __init__(self, strecke, koerpergewicht, skill_level, reisezeit=None):

        super().__init__(strecke, reisezeit)
        self.koerpergewicht = koerpergewicht
        self.skill_level = skill_level

    def berechne_kosten(self):
        met = 0  # MET = Metabolischer Äquivalent
        geschwindigkeit = 0

        if self.skill_level == 1:
            geschwindigkeit = 5  # km/h
            met = 2
        elif self.skill_level == 2:
            geschwindigkeit = 17.5  # km/h
            met = 6.3
        elif self.skill_level == 3:
            geschwindigkeit = 41.4  # km/h
            met = 17
        # Berechnung Reisezeit (in Stunden)
        self.reisezeit = self.strecke / geschwindigkeit
        # Berechnung kalorienverbrauch
        kalorienverbrauch = met * self.koerpergewicht * self.reisezeit
        # Berechnung Kosten anhand von Döner
        doener_preis = 8  # Euro
        doener_kalorien = 700  # kcal
        anzahl_doener = kalorienverbrauch / doener_kalorien
        kosten = anzahl_doener * doener_preis
        return kalorienverbrauch, kosten, self.reisezeit, anzahl_doener
        # Rückgabewert, damit das Ergebnis der Kostenberechnung außerhalb der Funktion/Klasse verwendet werden kann

    def ausgabe_details(self):
        kalorienverbrauch, kosten, reisezeit, anzahl_doener = self.berechne_kosten()
        print(
            f"Die Kosten für die Fahrradfahrt betragen{kosten: .2f} Euro bei einer Reisezeit von{reisezeit: .2f}"
            f" Stunden."
            f"\nDies entsprechen{anzahl_doener: .0f} Döner bei einem Durchschnittspreis von 8 Euro.")


# Unterklasse Bus
class Bus(Transportmittel):
    def __init__(self, strecke, reisezeit, ticketpreis):
        super().__init__(strecke, reisezeit)
        self.ticketpreis = ticketpreis

    def berechne_kosten(self):
        return self.ticketpreis

    def ausgabe_details(self):
        kosten = self.berechne_kosten()
        print(f"Die Kosten für die Busfahrt betragen{kosten: .2f} Euro bei einer Reisezeit von{self.reisezeit: .2f}"
              f" Stunden.")


class Zug(Transportmittel):
    def __init__(self, strecke, reisezeit, ticketpreis):
        super().__init__(strecke, reisezeit)
        self.ticketpreis = ticketpreis

    def berechne_kosten(self):
        return self.ticketpreis

    def ausgabe_details(self):
        kosten = self.berechne_kosten()
        print(f"Die Kosten für die Zugfahrt betragen{kosten: .2f} Euro bei einer Reisezeit von{self.reisezeit: .2f}"
              f" Stunden.")


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
