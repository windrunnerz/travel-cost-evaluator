# 🗺️ Roadmap für Web UI

## ✅ 1️⃣ Input- & Fehler-Handling

- **Frontend-Validierung einbauen**  
  Prüfen, ob Felder gefüllt sind, nur Zahlen, keine negativen Werte.

- **Backend-Validierung verbessern**  
  Flask: Eingehende Daten auf Typ & Werte prüfen, bei Fehler saubere JSON-Fehlerantwort.

---

## ✅ 2️⃣ Backend modularisieren

- **Blueprints nutzen**  
  Flask-API in separate Module teilen (z. B. `/api`, `/frontend`).

- **Utility-Funktionen auslagern**  
  Berechnungslogik in eigene Python-Datei (z. B. `utils.py`).

---

## ✅ 3️⃣ Tests einführen

- **Backend-Tests mit Pytest**  
  Routen testen (Statuscode, richtige Antworten).

- **Optionale JS-Tests** (später)  
  Basic Tests für API-Calls (z. B. mit Jest, falls du willst).

---

## ✅ 4️⃣ Frontend verbessern

- **Styling optimieren**  
  CSS oder Framework (z. B. Bootstrap), Buttons, Inputs schöner gestalten.

- **Ergebnisdarstellung verbessern**  
  Klarere Anzeige, evtl. farblich hervorheben.

---

## ✅ 5️⃣ Neue Features

- **Neue Transport-Optionen**  
  Fahrrad, Bahn, Carsharing, etc.

- **Zusätzliche Berechnungen**  
  CO₂-Ausstoß, Reisezeit, Parkkosten.

---

## ✅ 6️⃣ Dokumentation & Deployment

- **Readme ausbauen**  
  Anleitung, Screenshots, Feature-Liste.

- **Projekt deployen**  
  Z. B. Render, Fly.io oder Railway, damit du einen Live-Link hast.

