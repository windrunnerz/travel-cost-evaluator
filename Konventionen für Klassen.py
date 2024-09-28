"""
1. Klassen-Namen: CamelCase
    - Klassen-Namen sollten in CamelCase geschrieben werden, wobei jedes Wort im Namen großgeschrieben
    wird und keine Unterstriche (_) verwendet werden."""
class ReiseKosten:
    pass

class AutoTransport:
    pass

"""
2. Methoden- und Attributnamen: snake_case
    - Methoden und Attribute innerhalb einer Klasse sollten im snake_case geschrieben werden, d.h.
    nur Kleinbuchstaben mit Unterstrichen zwischen Wörtern"""
class Auto:
    def berechne_kosten(self):
        pass

    def anzahl_sitze(self):
        pass

"""
3. Klassen-Dokumentation
    - Füge einen Docstring (Dokumentations-String) direkt nach der Klassendefinition ein, um die Klasse
    zu beschreiben. Dies ist nützlich um anderen Entwicklern den Zweck und die Funktionsweise der
    Klasse zu erläutern."""
class Auto:
    """Diese Klasse repräsentiert ein Auto mit bestimmten Eigenschaften und Methoden zur Berechnung der Reisekosten."""

"""
4. Private Attribute und Methoden
    - Wenn ein Attribut oder eine Methode nur innerhalb der Klasse verwendet werden soll (also "privat"
    ist, verwende ein Unterstrich (_) am Anfang des Namens."""
class Auto:
    def __init__(self, strecke):
        self._strecke = strecke  # Privates Attribut

    def _interne_methode(self):  # Private Methode
        pass

"""
Zusammenfassung:
    - Klassen-Namen: CamelCase
    - Methoden- und Attributnamen: snake_case
    - Dokumentation: Docstrings, um Klassen und Methoden zu beschreiben
    - Private Attribute/Methoden: mit Unterstrich (_) beginnen → wird intern verwendet (innerhalb
    einer Klasse)
"""