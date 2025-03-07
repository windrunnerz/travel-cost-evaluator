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
