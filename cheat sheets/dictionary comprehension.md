✅ Definition:
    Comprehension bedeutet:  
    Kompakte, direkte Schreibweise, um aus einer bestehenden Datenstruktur (z.B. einer Liste oder einem Dictionary)
    eine neue Datenstruktur zu erstellen – oft mit Bedingungen und/oder Veränderungen.

✅ Aufbau einer Dictionary Comprehension:
```
{schlüssel: wert for schlüssel, wert in quelle if bedingung}
```
schlüssel und wert → werden übernommen oder verändert.  
quelle → ist das Dictionary, aus dem du die Daten ziehst.  
if bedingung (optional) → filtert, welche Einträge übernommen werden.

✅ Klassisch geschrieben:

```python
argumente = {}
for k, v in benutzer_eingaben.items():  # 🔹
    if k != "transportmittel":  
        argumente[k] = v    # Im Dictionary argumente soll unter dem Schlüssel k der Wert v gespeichert werden. 

```
✅ Genau dasselbe als Dictionary Comprehension:
```python
argumente = {k: v for k, v in benutzer_eingaben.items() if k != "transportmittel"}
```
🔹 Warum braucht man k, v?  
Die Methode items() gibt ein Wertepaar key und value als Tuple zurück.  
```python
("strecke", 100)
```
Mit zwei Variablen wird der Tupel direkt entpackt und man
kann einzeln mit key und value weiterarbeiten.  
`k = Schlüssel, v = Wert`

`argumente = {k: v for ...}` -> Baue ein neues dict argumente aus diesen Wertepaaren, Kurzform von `argumente[k] = v `