"""Hilfsfunktionen für backend"""

from flask import current_app

def berechne_kosten_pro_person(gesamtkosten: float, mitfahrer: int) -> float:
    anzahl = max(1, mitfahrer)
    return round( gesamtkosten / anzahl)

def convert_snake_to_camel(snake_dict: dict) -> dict:
    current_app.logger.debug("convert_snake_to_camel input: %s", snake_dict)
    current_app.logger.debug("Type: %s", type(snake_dict))
    camel_dict = {}

    for key, value in snake_dict.items():
        components = key.split('_')
        camel_key = components[0] + ''.join(x.title() for x in components[1:])
        camel_dict[camel_key] = value

    return camel_dict