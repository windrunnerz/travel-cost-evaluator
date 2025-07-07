from . import Auto, Fahrrad, Bus, Zug


def create_transportmittel(typ_or_dict):
    klassen_mapping = {
        "auto": Auto,
        "fahrrad": Fahrrad,
        "bus": Bus,
        "zug": Zug
    }
    # CLI-Modus: dict übergeben
    if isinstance(typ_or_dict, dict):
        typ = typ_or_dict["transportmittel"]
        argumente = {k: v for k, v in typ_or_dict.items() if k != "transportmittel"}
        return klassen_mapping[typ](**argumente)
   
    # Web-Modus: typ als String übergeben
    typ = typ_or_dict
    return klassen_mapping[typ]
