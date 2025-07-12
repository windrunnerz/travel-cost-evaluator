from src.transportmittel import Transportmittel


class Zug(Transportmittel):
    def __init__(self, strecke, reisezeit, ticket_preis):
        super().__init__(strecke, reisezeit)
        self.ticket_preis = ticket_preis

    def berechne_kosten(self):
        return float(self.ticket_preis)

    def ausgabe_details(self):
        kosten = self.berechne_kosten()
        print(f"Die Kosten für die Zugfahrt betragen{kosten: .2f} Euro bei einer Reisezeit von{self.reisezeit: .2f}"
              f" Stunden.")
