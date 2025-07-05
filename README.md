# Travel Cost Evaluator

**Ein Tool zur Berechnung und zum Vergleich von Reisekosten.**  
🔹 Du möchtest wissen, ob Auto, Zug oder Bus günstiger ist?  
🔹 Möchtest du schneller reisen und bist bereit, dafür mehr zu zahlen?  

Mit diesem Programm kannst du die Reisekosten für verschiedene Transportmittel ermitteln – passend zu deinem Budget.

## So funktioniert’s
![wireframe gif](https://github.com/user-attachments/assets/42685707-5df8-43e0-a32c-29aac425b682)

[Link zur wiki](https://github.com/windrunnerz/travel-cost-evaluator/wiki/Roadmap#geplante-gui-mockup)

## Installation
WIP

#  Projekt-Roadmap

## Ziel
* Dieses Projekt soll ein Tool zur Berechnung und zum Vergleich von Reisekosten bieten. 
* Der Nutzer kann angeben, welchen Aufpreis er für eine verkürzte Reisezeit akzeptiert.
* Zukünftige Features sollen die Benutzerfreundlichkeit verbessern und zusätzliche Transportmittel integrieren.

## Geplante Features/Tasks

### 🚧 In Arbeit
- [ ] Tests für alle Transportmittel-Klassen schreiben
- [ ] Verbesserung der Dokumentation (README, UML-Diagramme, Projekt-Doku, Code-Doku)
- [ ] Backend-Validierung verbessern (saubere Fehlerantworten in Flask)
- [ ] Frontend-Validierung ergänzen (z. B. keine negativen Werte, nur Zahlen)

### 🔜 Nächste Schritte
- [ ] API-Routen mit Flask Blueprints modularisieren
- [ ] Berechnungslogik in separates Python-Modul auslagern (z. B. `utils.py`)
- [ ] Speicherung von Berechnungen (optional JSON-Datei oder DB)
- [ ] Vergleich von zwei oder mehr Transportmitteln ermöglichen
- [ ] Weitere Transportmittel hinzufügen (Flugzeug, E-Scooter, Carsharing)
- [ ] GUI-Implementierung mit PySide6
- [ ] Benutzerfreundlichere CLI-Eingaben
- [ ] Kernlogik kapseln → eigenes Modul für Berechnungen (in Kombi mit `utils.py`)
- [ ] Frontend Styling verbessern (CSS oder Framework)
- [ ] Ergebnisdarstellung verbessern (z. B. farbliche Hervorhebung)
- [ ] Deployment vorbereiten (z. B. Render, Fly.io)

### ✅ Abgeschlossen
- [x] Factory Pattern für Transportmittel implementiert
- [x] Modularisierung des Codes
- [x] Refactor: API & DOM in JS aufgeteilt
- [x] `ReiseIO`-Klasse optimieren und Unit-Tests schreiben
