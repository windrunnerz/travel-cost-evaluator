✅ Was ist das Factory Pattern?  
Das Factory Pattern ist ein Entwurfsmuster (Design Pattern), das sich um die Erzeugung von Objekten kümmert. Sie ist 
eine zentrale Stelle (die „Factory“), die entscheidet, welche Klasse instanziiert werden soll – abhängig von bestimmten 
Bedingungen.

✅ Zweck des Factory Pattern  
🔹 Zentrale Steuerung:  
Die gesamte Logik zur Objekterstellung ist an einer Stelle gebündelt.

🔹 Wartbarkeit:  
Wenn du ein neues Transportmittel hinzufügst (z.B. „Flugzeug“), musst du den Code nur in der Factory erweitern – nicht 
überall sonst im Projekt.

🔹 Vermeidung von Wiederholung:  
Du brauchst nicht mehrfach die gleichen if-elif-else-Ketten für die Erstellung von Transportmitteln.

🔹 Sauberer Code:  
Deine main.py bleibt minimal und übersichtlich. Sie sagt nur noch:
„Hier sind die Eingaben – Factory, mach den Rest.“

✅ Wo das Factory Pattern sinnvoll ist:  

| Situation                                                   | Factory Pattern sinnvoll? |
|:------------------------------------------------------------|:--------------------------|
| Immer das gleiche Objekt mit festen Werten                  | ❌ Nein                    |
| Je nach Eingabe wird ein anderes Objekt gebraucht           | ✅ Ja                      |
| Du planst Erweiterungen, die neue Klassen einfügen          | ✅ Ja                      |
| Du willst die Erstellung austauschbar oder dynamisch machen | ✅ Ja                      |
| Nur eine einzige Klasse, feste Werte                        | ❌ Nein                    |

