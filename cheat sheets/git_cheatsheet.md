# 💣 Git Cheatsheet (Kurz & Klar)

## ✅ Branches

- **Branch erstellen und wechseln**

  ```bash
  git checkout -b feature/neuer-branch
  ```

- **Branch umbenennen (lokal)**

  ```bash
  git branch -m neuer-name
  ```

- **Branch löschen (lokal)**

  ```bash
  git branch -d branch-name
  ```

- **Branch löschen (remote)**

  ```bash
  git push origin --delete branch-name
  ```

- **Remote-Branches anzeigen**

  ```bash
  git branch -r
  ```

- **Alle Branches anzeigen (lokal & remote)**

  ```bash
  git branch -a
  ```

- **Upstream-Branch setzen (tracking)**

  ```bash
  git push --set-upstream origin branch-name
  ```

- **Upstream entfernen**

  ```bash
  git branch --unset-upstream
  ```

## ✅ Commit & Push

- **Änderungen hinzufügen (stagen)**

  ```bash
  git add .
  # oder spezifische Datei:
  git add datei.js
  ```

- **Commit erstellen**

  ```bash
  git commit -m "Kurze, klare Nachricht"
  ```

- **Commit mit detailliertem Body**

  ```bash
  git commit
  # Dann Editor öffnen, ausführlich schreiben
  ```

- **Pushen**

  ```bash
  git push
  ```

## ✅ Status & Log

- **Status anzeigen**

  ```bash
  git status
  ```

- **Commit-History anzeigen (kurz)**

  ```bash
  git log --oneline
  ```

- **Commit-History mit Details**

  ```bash
  git log
  ```

## ✅ Reset & Änderungen rückgängig

- **Letzten Commit rückgängig machen (Änderungen behalten)**

  ```bash
  git reset --soft HEAD~1
  ```

- **Letzten Commit rückgängig machen (Änderungen verwerfen)**

  ```bash
  git reset --hard HEAD~1
  ```

- **Geänderte Datei zurücksetzen (seit letztem Commit)**

  ```bash
  git checkout -- datei.js
  ```

## ✅ Remote

- **Remote anzeigen**

  ```bash
  git remote -v
  ```

- **Details anzeigen**

  ```bash
  git remote show origin
  ```

## ✅ Fetch & Pull

- **Remote-Änderungen holen (aber nicht mergen)**

  ```bash
  git fetch
  ```

- **Remote-Änderungen holen und mergen**

  ```bash
  git pull
  ```

---

⚡ **Merke:**

- **"fetch"** = nur holen.
- **"pull"** = holen & mergen.
- **"push"** = hochladen.
- **"commit"** = Snapshot lokal speichern.

💥 **Immer erst **``** checken, bevor du pushst oder resettest!**

