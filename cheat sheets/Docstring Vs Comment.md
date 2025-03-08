## ✅ Ein Docstring in Python ist eine spezielle Zeichenkette (String), die direkt unter einer Klasse, Funktion oder Methode steht, um sie zu dokumentieren.
Python nutzt dafür dreifache Anführungszeichen (`"""` oder `'''`), um mehrzeilige Beschreibungen zu ermöglichen.

### 🔍 Aufbau eines Docstrings
| Abschnitt                            | Bedeutung                                               |
|--------------------------------------|---------------------------------------------------------|
| Kurzbeschreibung                     | Eine 1–2-zeilige Erklärung, was die Klasse/Methode tut. |
| Detaillierte Beschreibung (optional) | Weitere Infos, z. B. besondere Hinweise.                |
| Args: (optional)                     | Welche Parameter die Funktion erwartet.                 |
| Attributes: (optional, für Klassen)  | Welche Attribute die Klasse speichert.                  |
| Returns: (optional)                  | Was die Methode zurückgibt.                             |
| Raises: (optional)                   | Welche Fehler die Methode auslösen kann.                |

### 🔍 Detailanalyse
1️⃣ Kurzbeschreibung
* Immer in der ersten Zeile des Docstrings.
* Sollte knapp und direkt sagen, was die Methode oder Klasse tut.

2️⃣ Detaillierte Beschreibung (optional)
* Falls nötig, kannst du hier mehr über die Klasse/Methode schreiben.
* Zum Beispiel Sonderfälle, Einschränkungen oder wichtige Hinweise.
```python
"""
Repräsentiert ein Auto als Transportmittel.

Diese Klasse speichert die notwendigen Werte, um die Fahrtkosten zu berechnen.
"""
```

3️⃣ Args: → Methodenparameter beschreiben
* Erklärt die Eingabeparameter.
* Schreibt den Typ und eine kurze Beschreibung
```python
Args:
    strecke (float): Die Strecke in Kilometern.
    spritkosten (float): Preis pro Liter Sprit in Euro.
    verbrauch (float): Verbrauch in Litern pro 100 km.
```

4️⃣ Attributes: → Klassenattribute beschreiben
* Gilt für Klassen-Docstrings.
* Erklärt, welche Werte die Klasse speichert.
```python
Attributes:
    strecke (float): Die zurückgelegte Strecke.
    spritkosten (float): Die Kosten pro Liter Sprit.
    verbrauch (float): Der Spritverbrauch pro 100 km.
```

5️⃣ Returns: → Rückgabewert einer Methode
* Nur für Methoden, die etwas zurückgeben.
* Beschreibt den Datentyp und die Bedeutung der Rückgabe.
```python
Returns:
    float: Die berechneten Spritkosten in Euro.
```

6️⃣ Raises: → Fehler, die auftreten können
* Nur falls eine Methode Fehler (raise) wirft.
* Beschreibt, welcher Fehler wann auftritt.
```python
Raises:
    ValueError: Falls die Strecke negativ ist.
```
Beispiel im Code:
```python
def set_strecke(self, wert):
    """
    Setzt die Strecke.

    Args:
        wert (float): Die neue Strecke in Kilometern.

    Raises:
        ValueError: Falls die Strecke negativ ist.
    """
    if wert < 0:
        raise ValueError("Strecke kann nicht negativ sein!")
    self.strecke = wert
```
🔍 Wann solltest du Attributes: nutzen?

| ❓ Situation                                                         | 🔥 Empfehlung                                        |
|---------------------------------------------------------------------|------------------------------------------------------|
| Alle Attribute sind selbsterklärend?                                | ❌ `Attributes`: kann weggelassen werden.             |
| Einige Attribute sind offensichtlich, aber eins ist komplex?	       | ✅ Beschreibe nur das nicht offensichtliche Attribut. |
| Mehrere Attribute haben spezielle Bedeutungen oder Einschränkungen? | ✅ Attributes: für alle relevanten Attribute nutzen.  |
| Die Attribute sind von außen zugänglich (self.xyz)	                 | ✅ Falls externe Nutzer den Code verwenden.           |
| Die Attribute werden nur intern genutzt (self._xyz)	                | ❌ Attributes: meist nicht nötig.                     |

🎯 Best Practices für Docstrings  
✅ Kurz, aber informativ.  
✅ Immer die Parameter (Args:) und Rückgabewerte (Returns:) dokumentieren.  
✅ Kein überflüssiger Code, nur relevante Infos.  
✅ „Selbsterklärender Code braucht weniger Doku“ – unnötige Docstrings vermeiden.  

## Beispiel für den Unterschied zwischen Docstrings und normalen Kommentaren

Normale Kommentare beginnen mit # und dienen zur Erklärung von Code-Details
Sie sind nur für den Entwickler sichtbar und helfen beim Verständnis des Codes
```python
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
```

Normale Kommentare können überall im Code verwendet werden  
Hier wird ein Objekt der Klasse Auto erstellt
```python
auto1 = Auto("BMW", "X5")
auto1.beschreibe()
```
Mit der help()-Funktion kann der Docstring angezeigt werden
help(Auto)

## help()
✅ help() ist ein eingebautes Python-Tool, das dir die Dokumentation (Docstrings) einer Klasse, Funktion oder eines 
Moduls anzeigt.  

🔍 Was macht help()?
* Es zeigt die Docstrings einer Klasse, Funktion oder eines Moduls direkt im Terminal an.
* Es hilft Entwicklern, den Code zu verstehen, ohne in die Datei schauen zu müssen.
* Es nutzt die Docstrings, die du in deinem Code geschrieben hast.

✅ Wo sollte man help() nutzen?  
🔍 1. help() in der interaktiven Konsole nutzen  
Wenn du wissen willst, wie eine Klasse oder Funktion funktioniert, kannst du help() direkt im Python-Interpreter oder 
im Terminal aufrufen:
```bash
python
```
Dann im laufenden Python-Interpreter:
```python
from src import Fahrrad
help(Fahrrad)
```
🔍 2. help() in einem separaten Skript nutzen (z.B. debug.py)  
Falls du oft help() für viele Dinge brauchst, kannst du ein eigenes Hilfsmodul (debug.py) erstellen:

📌 Datei: `debug.py`
```python
from src import Fahrrad, Auto

help(Fahrrad)
help(Auto)
```
Dann kannst du es in PyCharm oder über das Terminal ausführen:
```bash
python debug.py
```

🎯 Fazit  
* help() ist ein schnelles Nachschlagewerk für Klassen, Methoden und Funktionen.
* Es zeigt Docstrings, wenn sie vorhanden sind.
* Es spart Zeit, weil du nicht in den Code springen musst.
* Besonders nützlich, wenn du mit fremdem Code oder externen Bibliotheken arbeitest.