class Transportmittel:
    def __init__(self, strecke, reisezeit):
        self.strecke = strecke
        self.reisezeit = reisezeit

    def berechne_kosten(self):
        raise NotImplementedError("Diese Methode muss in der Unterklasse implementiert werden.")

class Auto(transportmittel):
    def __init__(self, strecke, reisezeit, spritkosten, verbrauch):
        super().__init__(strecke, reisezeit)
        self.spritkosten = spritkosten
        self.verbrauch = verbrauch

    def berechne_kosten(self):
        return (self.strecke / 100) * self.verbrauch * self.spritkosten

# Hauptprogramm
reise_io = ReiseIO()
eingaben = reise_io.eingabe()

# Erzeugt ein Auto-Objekt, falls das Transportmittel "auto" ist
if eingaben["transportmittel"] == "auto":
    auto1 = auto(strecke=eingaben["strecke"], reisezeit=eingaben["reisezeit"], spritkosten=eingaben["spritkosten"], verbrauch=eingaben["verbrauch"])
    kosten = auto1.berechne_kosten()
    reise_io.ausgabe(kosten)
