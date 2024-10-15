# transportmittel: bus, bahn, auto, flugzeug, fahrrad, zu fuss, e-scooter
# Oberklasse
class Transportmittel:
    """Berechnet Reisekosten für verschiedene Transportmittel"""

    def __init__(self, strecke, reisezeit):
        self.strecke = strecke
        self.reisezeit = reisezeit

    '''Platzhalter, abstrakte Methode die signalisiert,dass jede Unterklasse ihre eigene Implementierung dieser Methode bereitstellen muss.
    NotImplementedError ist eine eingebaute Exception-Klasse in Python -> signalisiert Fehlerzustände'''
    def berechne_kosten(self):
        raise NotImplementedError("Diese Methode muss in der Unterklasse implementiert werden.")


# Unterklasse Auto
class Auto(Transportmittel):
    def __init__(self, strecke, reisezeit, spritkosten, verbrauch):
        # region super()
        """super() ruft den Konstruktor der Oberklasse auf, 'strecke' und 'reisezeit' werden korrekt initialisiert und stehen der Unterklasse zur Verfügung"""
        # endregion
        super().__init__(strecke, reisezeit)
        '''Zuweisung der Parameter zu dem Attribut der Klasse auto. Der Wert von spritkosten wird in das Attribut self.spritkosten gespeichert. Durch das 
        Präfix self. wird das Attribut dem aktuellen Objekt der Klasse zugeordnet'''
        self.spritkosten = spritkosten
        self.verbrauch = verbrauch

    def berechne_kosten(self):
        # region Rückgabewert
        """Rückgabewert, damit das Ergebnis der Kostenberechnung außerhalb der Funktion/Klasse verwendet werden kann"""
        # endregion
        return (self.strecke / 100) * self.verbrauch * self.spritkosten


# Unterklasse Fahrrad
class Fahrrad(Transportmittel):
    def __init__(self, strecke, koerpergewicht, skill_level, reisezeit=None):
        # region super()
        """super() ruft den Konstruktor der Oberklasse auf, 'strecke' und 'reisezeit' werden korrekt initialisiert
        und stehen der Unterklasse zur Verfügung """
        # endregion
        super().__init__(strecke, reisezeit)
        '''Zuweisung der Parameter zu dem Attribut der Klasse auto. Der Wert von spritkosten wird in das Attribut 
        self.spritkosten gespeichert. Durch das Präfix self. wird das Attribut dem aktuellen Objekt der Klasse 
        zugeordnet '''
        self.koerpergewicht = koerpergewicht
        self.skill_level = skill_level

    def berechne_kosten(self):
        # MET = Metabolischer Äquivalent
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
        # region Rückgabewert
        """Rückgabewert, damit das Ergebnis der Kostenberechnung außerhalb der Funktion/Klasse verwendet werden kann"""
        # endregion
        return kalorienverbrauch, kosten, self.reisezeit, anzahl_doener


# Unterklasse Bus
class Bus(Transportmittel):
    def __init__(self, strecke, reisezeit, ticketpreis):
        super().__init__(strecke, reisezeit)
        self.ticketpreis = ticketpreis

    def berechne_kosten(self):
        return self.ticketpreis

# _____________________________________________________________________________
class ReiseIO:
    """Nimmt Benutzereingaben an und gibt die Gesamtkosten aus"""

    # region static method
    """static method arbeitet unabhängig von einer Klasseninstanz, d.h. sie benötigt keinen Zugriff auf Instanzvariablen
    (self) oder Klassenvariablen (cls). Die Methode verarbeitet nur Eingabedaten und gibt sie wieder zurück"""

    # endregion
    @staticmethod
    def eingabe():
        # region while Schleife
        """unendliche Schleife bis "auto" eingegeben wird → wird mit return oder break verlassen"""
        # endregion
        while True:
            # region replace
            """Fehler abfangen wenn ',' anstatt '.' für Kommazahlen eingegeben wird"""
            # endregion
            # evtl. Validierungen hinzufügen für mehrere Transportmittel
            transportmittel = input("Gebe das Transportmittel ein (nur Auto, Bus oder Fahrrad möglich!): ").lower()

            reisezeit = None    # Standardmäßig reisezeit initialisieren
            if transportmittel == "auto":
                # region .lower
                '''.lower wandelt Eingabe in Kleinbuchstaben um -> für Validierung sinnvoll, da einheitlich'''
                # endregion
                strecke = float(input("Gebe die Strecke in km ein: ").replace(',', '.'))
                reisezeit = float(input("Gebe die Reisezeit in Stunden ein: ").replace(',', '.'))

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
            else:
                print("Transportmittel nur Auto, Bus oder Fahrrad möglich! Bitte erneut eingeben.")

    # region Parameter kosten
    '''kosten wird in berechne_kosten() der class Auto berechnet und in kosten gespeichert. Der Parameter in
    ausgabe(kosten) ist notwendig, da die Methode ausgabe selbst nicht direkt Zugriff auf andere Methoden oder
    Daten hat. Ohne diesen Parameter würde die Methode nicht wissen, welchen Wert sie ausgeben soll.'''

    # endregion
    @staticmethod
    def ausgabe(transportmittel, kosten, reisezeit=None, anzahl_doener=None, ticketpreis=None):
        if transportmittel == "auto":
            print(f"Die Gesamtkosten betragen: {kosten:.2f} Euro.")
        elif transportmittel == "fahrrad":
            print(
                f"Die Kosten für die Fahrradfahrt betragen {kosten:.2f} Euro bei einer Reisezeit von {reisezeit:.2f} Stunden"
                f"\nDies entsprechen {anzahl_doener:.0f} Döner bei einem Durchschnittspreis von 8 Euro.")
        elif transportmittel == "bus":
            print(f"Die Kosten für die Busfahrt betragen {kosten:.2f} Euro bei einer Reisezeit von {reisezeit:.2f}.")
        else:
            print("Transportmittel nicht erkannt")


# Hauptprogramm
reise_io = ReiseIO()
benutzer_eingaben = ReiseIO.eingabe()

# region Object
'''Erzeugt ein Auto-Objekt, falls das Transportmittel "auto" ist'''
# endregion
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

# region lokale Variable
# keine lokalen Variablen definiert wie in Auto, deshalb muss aus dem dict die reisezeit übernommen werden, um
# korrekt an ausgabe() zu übergeben
# endregion
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

# Übergabe testen
# auto1 = auto(strecke=100, reisezeit=25, spritkosten=1.63, verbrauch=4.8)
# kosten = auto1.berechne_kosten()
