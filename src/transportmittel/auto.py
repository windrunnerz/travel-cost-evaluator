from src.transportmittel import Transportmittel


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

    def berechne_kosten(self) -> float:
        return (self.strecke / 100) * self.verbrauch * self.spritkosten
        # Rückgabewert, damit das Ergebnis der Kostenberechnung außerhalb der Funktion/Klasse verwendet werden kann

    def ausgabe_details(self):
        kosten = self.berechne_kosten()
        print(f"Das Auto fährt {self.strecke} km in {self.reisezeit} Stunden.")
        print(f"Die Gesamtkosten betragen: {kosten: .2f} Euro.")