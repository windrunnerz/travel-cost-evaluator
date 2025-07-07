"""Zentrales Modul zum steuern der Kommunikation zwischen Backend und Frontend"""

from .transportmittel.transportmittel import TransportmittelProtocol
from .transportmittel_factory import create_transportmittel
from .utils import berechne_kosten_pro_person


history_list = []

def berechne_reisekosten_service(fahrzeug_typ, strecke, reisezeit, verbrauch, sprtikosten, mitfahrer) -> dict:
    """
    Erzeugt das passende Transportmittel-Objekt, führt die Kostenberechnung aus 
    und gibt das Ergebnis als Dictionary zurück.

    Die Berechnung der Gesamtkosten erfolgt in der jeweiligen Transportmittel-Klasse.
    Die Aufteilung auf Mitfahrer erfolgt hier im Service.
    """
    if fahrzeug_typ == "auto":
        fahrzeug_klasse = create_transportmittel(fahrzeug_typ)
        auto_objekt: TransportmittelProtocol = fahrzeug_klasse(strecke,
                                                               reisezeit,
                                                               verbrauch,
                                                               sprtikosten)
        gesamtkosten = auto_objekt.berechne_kosten()
        assert isinstance(gesamtkosten, float)
        kosten_pro_person = berechne_kosten_pro_person(gesamtkosten, mitfahrer)

        return {
            "gesamtkosten": round(gesamtkosten),
            "kosten_pro_person": kosten_pro_person
        }
   
    elif fahrzeug_typ == "fahrrad":
        fahrzeug_klasse = create_transportmittel(fahrzeug_typ)
        fahrrad_objekt: TransportmittelProtocol = fahrzeug_klasse(strecke, 
                                                                  reisezeit, 
                                                                  verbrauch, 
                                                                  sprtikosten)
        result = fahrrad_objekt.berechne_kosten()
        return result
  
    elif fahrzeug_typ == "bus":
        fahrzeug_klasse = create_transportmittel(fahrzeug_typ)
        bus_objekt: TransportmittelProtocol = fahrzeug_klasse(strecke, 
                                                              reisezeit, 
                                                              verbrauch, 
                                                              sprtikosten)
        result = bus_objekt.berechne_kosten()
        return result
   
    elif fahrzeug_typ == "zug":
        fahrzeug_klasse = create_transportmittel(fahrzeug_typ)
        zug_objekt: TransportmittelProtocol = fahrzeug_klasse(strecke, 
                                                              reisezeit, 
                                                              verbrauch, 
                                                              sprtikosten)
        result = zug_objekt.berechne_kosten()
        return result
   
    else:
        raise ValueError(f"Unbekannter Fahrzeugtyp: {fahrzeug_typ}")