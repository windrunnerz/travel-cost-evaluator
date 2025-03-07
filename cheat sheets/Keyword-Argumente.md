✅ Was sind benannte Argumente?  
Benannte Argumente (auch „Keyword-Argumente“ genannt) sind Argumente, die du beim Funktions- oder Methodenaufruf 
explizit mit Namen angibst.
Dadurch weiß Python genau, welcher Wert zu welchem Parameter gehört – unabhängig von der Reihenfolge.

🔍 Beispiel ohne benannte Argumente (nur Positionsargumente):  
```python
def auto_fahren(strecke, reisezeit):
    print(f"{strecke} km in {reisezeit} Stunden")
    
auto_fahren(100, 2)
```
Hier gilt:
* Wert → strecke  
* Wert → reisezeit  

Wenn du die Reihenfolge vertauschst, passiert Mist:
```python
auto_fahren(2, 100)
# 2 km in 100 Stunden (wohl kaum gewollt)
```

🔍 Beispiel mit benannten Argumenten:
```python
auto_fahren(strecke=100, reisezeit=2)
```
Hier sagst du explizit:  
* strecke = 100  
* reisezeit = 2

Keine Probleme bei anderer Reihenfolge.

✅ Warum ist das für **argumente wichtig?  
Weil **argumente genau so ein Dictionary ist:  
```python
argumente = {
    "strecke": 100,
    "reisezeit": 2
}
```
Und Auto(**argumente) wird dann zu:  
```python
Auto(strecke=100, reisezeit=2)
```
Python nimmt automatisch die Schlüssel als Namen der Argumente und die Werte als deren Inhalt.

🔔 Merksatz:  
**Benannte Argumente geben den Parametern beim Aufruf direkt Namen.
Dadurch sind sie unabhängig von der Reihenfolge und super für Klarheit, Verständlichkeit und Flexibilität.**

🔍 Wie heißt der **-Operator?  
Offiziell nennt man ihn in diesem Zusammenhang:

„Keyword-Argument-Entpacker“

Oder auch:

* „Double Star Operator“ (umgangssprachlich).  
* „Kwargs-Entpacker“ (nach dem üblichen Namen **kwargs).  
* „Doppelstern-Operator“ (eingedeutscht).  
Er signalisiert Python:

„Hier kommt ein Dictionary mit Schlüssel-Wert-Paaren, die ich als benannte Argumente an die Funktion/Klasse übergeben 
möchte.“  
In Doku, Tutorials und StackOverflow liest du meistens „Keyword Arguments“ oder „Kwargs“.