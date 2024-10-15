# transportmittel: bus, bahn, auto, flugzeug, fahrrad, zu fuss, e-scooter
# Oberklasse
class Transportmittel:
    """Berechnet Reisekosten für verschiedene Transportmittel"""

    def __init__(self, strecke, reisezeit):
        self.strecke = strecke
        self.reisezeit = reisezeit

    # Platzhalter, abstrakte Methode die signalisiert, dass jede Unterklasse ihre eigene Implementierung dieser
    # Methode bereitstellen muss. NotImplementedError ist eine eingebaute Exception-Klasse in Python → signalisiert
    # Fehlerzustände

    def berechne_kosten(self):
        raise NotImplementedError("Diese Methode muss in der Unterklasse implementiert werden.")


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


# Unterklasse Fahrrad
class Fahrrad(Transportmittel):
    def __init__(self, strecke, koerpergewicht, skill_level, reisezeit=None):

        super().__init__(strecke, reisezeit)
        self.koerpergewicht = koerpergewicht
        self.skill_level = skill_level

    def berechne_kosten(self):
        """MET = Metabolischer Äquivalent"""
        if self.skill_level == 1:
            geschwindigkeit = 5  # km/h
            MET = 2
        elif self.skill_level == 2:
            geschwindigkeit = 17.5  # km/h
            MET = 6.3
        elif self.skill_level == 3:
            geschwindigkeit = 41.4  # km/h
            MET = 17
        # Berechnung Reisezeit (in Stunden)
        self.reisezeit = self.strecke / geschwindigkeit
        # Berechnung kalorienverbrauch
        kalorienverbrauch = MET * self.koerpergewicht * self.reisezeit
        # Berechnung Kosten anhand von Döner
        doener_preis = 8  # Euro
        doener_kalorien = 700  # kcal
        anzahl_doener = kalorienverbrauch / doener_kalorien
        kosten = anzahl_doener * doener_preis
        return kalorienverbrauch, kosten, self.reisezeit, anzahl_doener
        # Rückgabewert, damit das Ergebnis der Kostenberechnung außerhalb der Funktion/Klasse verwendet werden kann


# Unterklasse Bus
class Bus(Transportmittel):
    def __init__(self, strecke, reisezeit, ticketpreis):
        super().__init__(strecke, reisezeit)
        self.ticketpreis = ticketpreis

    def berechne_kosten(self):
        return self.ticketpreis


class Zug(Transportmittel):
    def __init__(self, strecke, reisezeit, ticketpreis):
        super().__init__(strecke, reisezeit)
        self.ticketpreis = ticketpreis

    def berechne_kosten(self):
        return self.ticketpreis


# _____________________________________________________________________________
class ReiseIO:
    """Nimmt Benutzereingaben an und gibt die Gesamtkosten aus"""

    # static method arbeitet unabhängig von einer Klasseninstanz, d.h. sie benötigt keinen Zugriff auf Instanzvariablen
    # (self) oder Klassenvariablen (cls). Die Methode verarbeitet nur Eingabedaten und gibt sie wieder zurück"""
    @staticmethod
    def eingabe():
        # unendliche Schleife bis gültiges Transportmittel eingegeben wird → wird mit return oder break verlassen
        while True:

            transportmittel = input("Gebe das Transportmittel ein (nur Auto, Bus, Zug oder Fahrrad möglich!): ").lower()

            reisezeit = None  # Standardmäßig reisezeit initialisieren
            if transportmittel == "auto":
                strecke = float(input("Gebe die Strecke in km ein: ").replace(',', '.'))
                reisezeit = float(input("Gebe die Reisezeit in Stunden ein: ").replace(',', '.'))
                # Fehler abfangen, wenn ',' anstatt '.' für Kommazahlen eingegeben wird
                # .lower wandelt Eingabe in Kleinbuchstaben um → für Validierung sinnvoll, da einheitlich

            else:
                strecke = float(input("Gebe die Strecke in km ein: ").replace(',', '.'))

            # Transportmittel Auto → zusätzliche Eingaben verlangen
            if transportmittel == "auto":
                spritkosten = float(input("Wie viel kostet 1L Sprit?(z.B. 1,74): ").replace(',', '.'))
                verbrauch = float(input("Wie viel verbraucht das Auto auf 100km?: ").replace(',', '.'))
                return {
                    "transportmittel": transportmittel,
                    "strecke": strecke,
                    "reisezeit": reisezeit,
                    "spritkosten": spritkosten,
                    "verbrauch": verbrauch
                }
            # Transportmittel Fahrrad → zusätzliche Eingaben verlangen
            elif transportmittel == "fahrrad":
                koerpergewicht = float(input("Gebe dein Körpergewicht in kg ein: ").replace(',', '.'))
                skill_level = float(
                    input(f"Gebe dein Skill Level an (1, 2, 3): \n1: Dreirad\n2: Normal\n3: Triathlon-Profi\n"))
                return {
                    "transportmittel": transportmittel,
                    "strecke": strecke,
                    "koerpergewicht": koerpergewicht,
                    "skill_level": skill_level
                }
            # Transportmittel Bus -> Ticketpreis
            elif transportmittel == "bus":
                ticketpreis = float(input("Wie viel kostet das Busticket in Euro?: "))
                reisezeit = float(input("Wie lange dauert die Busfahrt in Stunden?: "))
                return {
                    "transportmittel": transportmittel,
                    "strecke": strecke,
                    "reisezeit": reisezeit,
                    "ticketpreis": ticketpreis
                }
            # Transportmittel Zug -> Ticketpreis
            elif transportmittel == "zug":
                ticketpreis = float(input("Wie viel kostet das Zugticket in Euro?: "))
                reisezeit = float(input("Wie lange dauert die Zugfahrt in Stunden?: "))
                return {
                    "transportmittel": transportmittel,
                    "strecke": strecke,
                    "reisezeit": reisezeit,
                    "ticketpreis": ticketpreis
                }
            else:
                print("Transportmittel nur Auto, Bus, Zug oder Fahrrad möglich! Bitte erneut eingeben.")

    @staticmethod
    def ausgabe(transportmittel, kosten, reisezeit=None, anzahl_doener=None, ticketpreis=None):
        # kosten wird in berechne_kosten() der class Auto berechnet und in kosten gespeichert. Der Parameter in
        # ausgabe(kosten) ist notwendig, da die Methode ausgabe selbst nicht direkt Zugriff auf andere Methoden oder
        # Daten hat. Ohne diesen Parameter würde die Methode nicht wissen, welchen Wert sie ausgeben soll.
        if transportmittel == "auto":
            print(f"Die Gesamtkosten betragen: {kosten:.2f} Euro.")
        elif transportmittel == "fahrrad":
            print(
                f"Die Kosten für die Fahrradfahrt betragen {kosten:.2f} Euro bei einer Reisezeit von {reisezeit:.2f} Stunden "
                f"\nDies entsprechen {anzahl_doener:.0f} Döner bei einem Durchschnittspreis von 8 Euro.")
        elif transportmittel == "bus":
            print(f"Die Kosten für die Busfahrt betragen {kosten:.2f} Euro bei einer Reisezeit von {reisezeit:.2f}.")
        elif transportmittel == "zug":
            print(f"Die Kosten für die Zugfahrt betragen {kosten:.2f} Euro bei einer Reisezeit von {reisezeit:.2f}.")
        else:
            print("Transportmittel nicht erkannt")


# ____________________________________________________________________________________________________________________
# Hauptprogramm
reise_io = ReiseIO()
benutzer_eingaben = ReiseIO.eingabe()

# Erzeugt ein Objekt, je nach Transportmittel
if benutzer_eingaben["transportmittel"] == "auto":
    auto1 = Auto(strecke=benutzer_eingaben["strecke"],
                 reisezeit=benutzer_eingaben["reisezeit"],
                 spritkosten=benutzer_eingaben["spritkosten"],
                 verbrauch=benutzer_eingaben["verbrauch"]
                 )
    kosten = auto1.berechne_kosten()
    ReiseIO.ausgabe(benutzer_eingaben["transportmittel"], kosten)


elif benutzer_eingaben["transportmittel"] == "fahrrad":
    fahrrad1 = Fahrrad(strecke=benutzer_eingaben["strecke"],
                       koerpergewicht=benutzer_eingaben["koerpergewicht"],
                       skill_level=benutzer_eingaben["skill_level"])
    kalorienverbrauch, kosten, reisezeit, anzahl_doener = fahrrad1.berechne_kosten()
    ReiseIO.ausgabe(benutzer_eingaben["transportmittel"], kosten, reisezeit, anzahl_doener)


elif benutzer_eingaben["transportmittel"] == "bus":
    bus1 = Bus(strecke=benutzer_eingaben["strecke"],
               reisezeit=benutzer_eingaben["reisezeit"],
               ticketpreis=benutzer_eingaben["ticketpreis"]
               )
    kosten = bus1.berechne_kosten()
    ReiseIO.ausgabe(benutzer_eingaben["transportmittel"],
                    kosten,
                    benutzer_eingaben["reisezeit"],
                    benutzer_eingaben["ticketpreis"]
                    )
    # keine lokalen Variablen definiert wie in Auto, deshalb muss aus dem dict die reisezeit übernommen werden, um
    # korrekt an ausgabe() zu übergeben

elif benutzer_eingaben["transportmittel"] == "zug":
    zug1 = Zug(strecke=benutzer_eingaben["strecke"],
               reisezeit=benutzer_eingaben["reisezeit"],
               ticketpreis=benutzer_eingaben["ticketpreis"]
               )
    kosten = zug1.berechne_kosten()
    ReiseIO.ausgabe(benutzer_eingaben["transportmittel"],
                    kosten,
                    benutzer_eingaben["reisezeit"],
                    benutzer_eingaben["ticketpreis"]
                    )
# Übergabe testen
# auto1 = auto(strecke=100, reisezeit=25, spritkosten=1.63, verbrauch=4.8)
# kosten = auto1.berechne_kosten()


