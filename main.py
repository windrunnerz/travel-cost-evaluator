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
        return (self.strecke / 100) * self.verbrauch * self. spritkosten

# Unterklasse zu Fuss
class ZuFuss(Transportmittel):
    # Faktoren: körperliche Fitness, Alter, Steigung
    def __init__(self, strecke, reisezeit):
        geschwindigkeit = 5 # in km/h
        # region super()
        """super() ruft den Konstruktor der Oberklasse auf, 'strecke' und 'reisezeit' werden korrekt initialisiert und stehen der Unterklasse zur Verfügung"""
        # endregion
        super().__init__(strecke, reisezeit)

    def berechne_kosten(self):
        # region Rückgabewert
        """Rückgabewert, damit das Ergebnis der Kostenberechnung außerhalb der Funktion/Klasse verwendet werden kann"""
        # endregion
        return (self.strecke / 100) * self.verbrauch * self. spritkosten
#_____________________________________________________________________________
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
            strecke = float(input("Gebe die Strecke in km ein: ").replace(',', '.'))
            reisezeit = float(input("Gebe die Reisezeit in Stunden ein: ").replace(',', '.'))
            # region .lower
            '''.lower wandelt Eingabe in Kleinbuchstaben um -> für Validierung sinnvoll, da einheitlich'''
            # endregion
            transportmittel = input("Gebe das Transportmittel ein (nur Auto möglich!): ").lower()

            # Transportmittel Auto → zusätzliche Eingaben verlangen
            if transportmittel == "auto":
                spritkosten = float(input("Gebe die Spritkosten pro Liter ein: ").replace(',', '.'))
                verbrauch = float(input("Gebe den Verbrauch pro 100 km ein: ").replace(',', '.'))
                return {
                    "transportmittel": transportmittel,
                    "strecke": strecke,
                    "reisezeit": reisezeit,
                    "spritkosten": spritkosten,
                    "verbrauch": verbrauch
                }
            else:
                print("Transportmittel nur Auto möglich! Bitte erneut eingeben.")

    # region Parameter kosten
    '''kosten wird in berechne_kosten() der class Auto berechnet und in kosten gespeichert. Der Parameter in
    ausgabe(kosten) ist notwendig, da die Methode ausgabe selbst nicht direkt Zugriff auf andere Methoden oder
    Daten hat. Ohne diesen Parameter würde die Methode nicht wissen, welchen Wert sie ausgeben soll.'''
    # endregion
    @staticmethod
    def ausgabe(kosten):
        # region Formatierung
        """Formatierungsanweisungen nur möglich in f-strings oder der Methode format()"""
        # endregion
        print(f"Die Gesamtkosten betragen: {kosten:.2f} Euro.")

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
    ReiseIO.ausgabe(kosten)


# Übergabe testen
#auto1 = auto(strecke=100, reisezeit=25, spritkosten=1.63, verbrauch=4.8)
#kosten = auto1.berechne_kosten()

