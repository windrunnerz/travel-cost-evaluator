from abc import ABC, abstractmethod


# Oberklasse
class Transportmittel(ABC):
    """Berechnet Reisekosten für verschiedene Transportmittel"""

    def __init__(self, strecke, reisezeit):
        self.strecke = strecke
        self.reisezeit = reisezeit

    # Platzhalter, abstrakte Methode die signalisiert, dass jede Unterklasse ihre eigene Implementierung dieser
    # Methode bereitstellen muss. NotImplementedError ist eine eingebaute Exception-Klasse in Python → signalisiert
    # Fehlerzustände
    @abstractmethod
    def berechne_kosten(self):
        raise NotImplementedError("Diese Methode muss in der Unterklasse implementiert werden.")

    @abstractmethod
    def ausgabe_details(self):
        pass
    # @abstractmethod zeigt an, dass jede Unterklasse diese Methode implementieren muss
