"""Hilfsfunktionen für backend"""

def berechne_kosten_pro_person(gesamtkosten: float, mitfahrer: int) -> float:
    anzahl = max(1, mitfahrer)
    return round( gesamtkosten / anzahl)
