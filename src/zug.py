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
