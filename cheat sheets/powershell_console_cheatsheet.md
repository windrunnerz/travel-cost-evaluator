# ⚡ PowerShell & Console Cheatsheet (Kurz & Klar)

## ✅ Navigation & Verzeichnisse

- **Aktuelles Verzeichnis anzeigen**

  ```powershell
  pwd
  ```

- **Verzeichnis wechseln**

  ```powershell
  cd pfad/zum/ordner
  ```

- **Ein Verzeichnis nach oben gehen**

  ```powershell
  cd ..
  ```

- **In ein Unterverzeichnis springen (Tab-Completion!)**

  ```powershell
  cd src
  ```

- **Verzeichnisinhalt anzeigen**

  ```powershell
  ls
  ```

  oder

  ```powershell
  dir
  ```

## ✅ Dateien & Ordner

- **Datei erstellen (leer)**

  ```powershell
  ni datei.txt
  ```

- **Ordner erstellen**

  ```powershell
  mkdir neuerOrdner
  ```

- **Datei löschen**

  ```powershell
  rm datei.txt
  ```

- **Ordner löschen (rekursiv)**

  ```powershell
  rm -r ordnerName
  ```

## ✅ Dateiinhalt & Bearbeitung

- **Dateiinhalt anzeigen**

  ```powershell
  cat datei.txt
  ```

- **Datei öffnen (Standard-Editor)**

  ```powershell
  notepad datei.txt
  ```

## ✅ Prozesse & Tasks

- **Laufende Prozesse anzeigen**

  ```powershell
  Get-Process
  ```

- **Prozess beenden**

  ```powershell
  Stop-Process -Name "notepad"
  ```

## ✅ Sonstiges

- **Clear Screen (Konsole leeren)**

  ```powershell
  cls
  ```

- **Hilfe zu einem Befehl anzeigen**

  ```powershell
  get-help befehl
  ```

- **PowerShell-Version anzeigen**

  ```powershell
  $PSVersionTable
  ```

---

⚡ **Merke:**

- In PowerShell gibt es oft mehrere Aliase (z. B. `ls`, `dir`, `gci` = alle zeigen Inhalt).
- Tab-Completion spart Zeit!

💥 **Immer prüfen, in welchem Verzeichnis du bist, bevor du rm -r benutzt!**

