from abc import ABC, abstractmethod
from typing import Protocol


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


class TransportmittelProtocol(Protocol):
    """
    Definiert das Protokoll (Schnittstelle) für alle Transportmittel-Klassen.

    Jede Klasse, die dieses Protokoll erfüllen möchte, muss mindestens
    die Methode `berechne_kosten()` implementieren.

    Dies ermöglicht statisches Typ-Checking (z. B. mit Pylance) und
    IntelliSense-Unterstützung, ohne die konkrete Klasse vorher kennen zu müssen.
    """
    def berechne_kosten(self):
        ...