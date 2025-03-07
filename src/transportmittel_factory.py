from . import Auto, Fahrrad, Bus, Zug


def transportmittel_factory(benutzer_eingaben):
    typ = benutzer_eingaben["transportmittel"]

    klassen_mapping = {
        "auto": Auto,
        "fahrrad": Fahrrad,
        "bus": Bus,
        "zug": Zug
    }

    if typ not in klassen_mapping:
        raise ValueError(f"Unbekanntes Transportmittel: {typ}")

    argumente = {k: v for k, v in benutzer_eingaben.items() if k != "transportmittel"}

    return klassen_mapping[typ](**argumente)
