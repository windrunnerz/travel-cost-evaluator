class ZuFuss(Transportmittel):
    # Faktoren: körperliche Fitness, Alter, Steigung
    # doener kcal = 700 kcal
    def __init__(self, strecke, reisezeit):
        geschwindigkeit = 5 # in km/h
        # region super()
        """super() ruft den Konstruktor der Oberklasse auf, 'strecke' und 'reisezeit' werden korrekt initialisiert und stehen der Unterklasse zur Verfügung"""
        # endregion
        super().__init__(strecke, reisezeit)

    def berechne_kosten(self):
        # t = s / v
        # region Rückgabewert
        """Rückgabewert, damit das Ergebnis der Kostenberechnung außerhalb der Funktion/Klasse verwendet werden kann"""
        # endregion
        return self.strecke /


# geschwindigkeit, genaue anweisung bei auto, schmerzgrenze wie viel mehr zahlen für weniger kosten oder zeit
# wie viel ist dir zeit wert / was ist dir mehre wert zeit oder geld?