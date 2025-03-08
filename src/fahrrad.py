from .transportmittel import Transportmittel


class Fahrrad(Transportmittel):
    """
    Repräsentiert ein Fahrrad als Transportmittel.

    Attributes:
       skill_level (int): Der Erfahrungsgrad des Fahrers (1 = Anfänger, 2 = Normal, 3 = Profi).
    """
    def __init__(self, strecke, koerpergewicht, skill_level, reisezeit=None):
        """
        Initialisiert ein Fahrrad-Objekt.

        Args:
            skill_level (int): Fahrkönnen (1 = Anfänger, 2 = Normal, 3 = Profi).
        """
        super().__init__(strecke, reisezeit)
        self.koerpergewicht = koerpergewicht
        self.skill_level = skill_level

    def berechne_kosten(self):
        """
        Berechnet Kalorienverbrauch und hypothetischen Kosten.

        Die Berechnung basiert auf dem MET-Wert (Metabolisches Äquivalent der Aktivität)
        in Abhängigkeit vom `skill_level`. Die hypothetischen Kosten werden in Döner-Äquivalenten
        umgerechnet, basierend auf einer Standard-Dönergröße.
        """
        met = 0
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

        self.reisezeit = self.strecke / geschwindigkeit
        kalorienverbrauch = met * self.koerpergewicht * self.reisezeit

        doener_preis = 8  # Euro
        doener_kalorien = 700  # kcal
        anzahl_doener = kalorienverbrauch / doener_kalorien
        kosten = anzahl_doener * doener_preis

        return kalorienverbrauch, kosten, self.reisezeit, anzahl_doener


    def ausgabe_details(self):
        """
        Gibt die berechneten Werte für die Fahrradfahrt formatiert aus.
        """
        kalorienverbrauch, kosten, reisezeit, anzahl_doener = self.berechne_kosten()
        print(
            f"Die Kosten für die Fahrradfahrt betragen{kosten: .2f} Euro bei einer Reisezeit von{reisezeit: .2f}"
            f" Stunden."
            f"\nDies entsprechen{anzahl_doener: .0f} Döner bei einem Durchschnittspreis von 8 Euro.")
