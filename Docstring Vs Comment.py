# Beispiel für den Unterschied zwischen Dokstrings und normalen Kommentaren

# Normale Kommentare beginnen mit # und dienen zur Erklärung von Code-Details
# Sie sind nur für den Entwickler sichtbar und helfen beim Verständnis des Codes

class Auto:
    """
    Diese Klasse repräsentiert ein Auto und seine Eigenschaften.

    Dies ist ein Docstring. Er wird zur Dokumentation der Klasse verwendet.
    Der Docstring steht direkt nach der Klassendefinition und ist mit dreifachen Anführungszeichen geschrieben.
    """

    def __init__(self, marke, modell):
        """
        Initialisiert ein Auto mit Marke und Modell.

        Dies ist ein Dokstring für den Konstruktor der Klasse Auto.
        """
        self.marke = marke
        self.modell = modell  # Modell des Autos, normale Kommentare erklären Code-Details

    def beschreibe(self):
        """
        Gibt eine Beschreibung des Autos aus.

        Dies ist ein Dokstring für die Methode 'beschreibe'.
        """
        print(f"{self.marke} {self.modell}")


# Normale Kommentare können überall im Code verwendet werden
# Hier wird ein Objekt der Klasse Auto erstellt
auto1 = Auto("BMW", "X5")
auto1.beschreibe()

# Mit der help()-Funktion kann der Dokstring angezeigt werden
help(Auto)