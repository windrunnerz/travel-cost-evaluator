"""
Dieses Modul enthält die zentrale Service-Funktion `berechne_reisekosten_service`,
die die Verbindung zwischen der Transportmittel-Logik (z.B. Auto, Fahrrad, Bus, Zug)
und der Flask-Web-App herstellt.

Design-Prinzipien:
- Trennt Berechnungslogik (Transportmittel-Klassen) von der API-Schicht (web_app.py).
- Nimmt alle relevanten Parameter entgegen (je nach Fahrzeugtyp unterschiedlich).
- Berechnet Gesamtkosten über die jeweilige Transportmittel-Klasse.
- Verteilt optional die Kosten auf Mitfahrer (außer bei Fahrrad, dort meist irrelevant).
- Gibt ein standardisiertes Ergebnis-Dictionary zurück, das direkt an das Frontend
  weitergegeben werden kann.

Hinweis:
Für maximale Flexibilität sind manche Parameter optional und können mit Default-Werten
(z.B. mitfahrer=1) übergeben werden. Die konkrete Nutzung und Filterung der Parameter
erfolgt abhängig vom gewählten Fahrzeugtyp in web_app.py.
"""

import logging
from .transportmittel.transportmittel import TransportmittelProtocol
from .transportmittel_factory import create_transportmittel
from .utils import berechne_kosten_pro_person

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def berechne_reisekosten_service(
    fahrzeug_typ,
    strecke,
    reisezeit,
    verbrauch=None,
    spritkosten=None,
    mitfahrer=1,
    koerpergewicht=None,
    skill_level=None,
    ticket_preis=None
) -> dict:
    """
    Erzeugt das passende Transportmittel-Objekt, führt die Kostenberechnung aus 
    und gibt das Ergebnis als Dictionary zurück.

    Die Berechnung der Gesamtkosten erfolgt in der jeweiligen Transportmittel-Klasse.
    Die Aufteilung auf Mitfahrer erfolgt hier im Service.
    """

    match fahrzeug_typ:
        case "auto":
            auto_klasse = create_transportmittel(fahrzeug_typ)
            auto_objekt: TransportmittelProtocol = auto_klasse(
                strecke=strecke,
                reisezeit=reisezeit,
                verbrauch=verbrauch,
                spritkosten=spritkosten
            )
            gesamtkosten = auto_objekt.berechne_kosten()
            assert isinstance(gesamtkosten, float)
            kosten_pro_person = berechne_kosten_pro_person(gesamtkosten, mitfahrer)

            return {
                "gesamtkosten": round(gesamtkosten),
                "kostenProPerson": kosten_pro_person
            }
      
        case "fahrrad":
            fahrzeug_klasse = create_transportmittel(fahrzeug_typ)
            fahrrad_objekt: TransportmittelProtocol = fahrzeug_klasse(
                strecke=strecke,
                reisezeit=reisezeit,
                koerpergewicht=koerpergewicht,
                skill_level=skill_level
            )
            kalorienverbrauch, kosten, reisezeit, anzahl_doener = fahrrad_objekt.berechne_kosten() # type: ignore
            
            return {
                "kalorienverbrauch": kalorienverbrauch,
                "kosten": kosten,
                "reisezeit": reisezeit,
                "anzahlDoener": anzahl_doener
            }
            
        case "bus" | "zug":
            fahrzeug_klasse = create_transportmittel(fahrzeug_typ)
            fahrzeug_objekt: TransportmittelProtocol = fahrzeug_klasse(
                strecke=strecke,
                reisezeit= reisezeit,
                ticket_preis=ticket_preis
            )
            gesamtkosten = fahrzeug_objekt.berechne_kosten()
            assert isinstance(gesamtkosten, float)
            kosten_pro_person = berechne_kosten_pro_person(gesamtkosten, mitfahrer)

            return {
                "gesamtkosten": gesamtkosten,
                "kostenProPerson": kosten_pro_person
            }
        case _:
            raise ValueError(f"Unbekannter Fahrzeugtyp: {fahrzeug_typ}")
