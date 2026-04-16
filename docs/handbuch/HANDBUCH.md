# Handbuch

## 1. Zweck
Dieses Handbuch beschreibt Betrieb, Entwicklung, Qualitätssicherung und Wartung des Repositories.

## 2. Projektstart
1. Voraussetzungen prüfen:
   - Docker + Docker Compose verfügbar
2. Bootstrap ausführen:
   - bash scripts/bootstrap.sh
3. Services starten:
   - bash scripts/start-services.sh
4. Aufruf:
   - Frontend: http://localhost:8000
   - API-Dokumentation: http://localhost:5000/docs

## 3. Funktionsumfang
- Noteneingabe für BWL, Mathe, Deutsch, Englisch.
- Berechnung des Durchschnitts.
- Erkennung von Nachhilfebedarf für Noten > 4.0.
- Persistierung aller Berechnungen in MySQL.
- Abruf der letzten Berechnungen über API.

## 4. Qualitätssicherung
- Security-Gate:
  - bash scripts/validate-security.sh
- Architektur-Gate:
  - bash scripts/validate-architecture.sh
- Dokumentations-Gate:
  - bash scripts/validate-docs.sh
- Unit Tests API:
  - cd services/python-api && pytest

## 5. Wartung
- Abhängigkeiten regelmäßig aktualisieren.
- Sicherheitsprüfskripte vor jedem Release ausführen.
- Legacy-Uploads nur im vorgesehenen Verzeichnis analysieren.
- Dokumentation bei Struktur- oder Funktionsänderungen aktualisieren.

## 6. Troubleshooting
- API nicht erreichbar:
  - docker compose ps prüfen
  - docker compose logs python-api prüfen
- Datenbankfehler:
  - docker compose logs mysql prüfen
- Frontend zeigt keine Ergebnisse:
  - Browser-Konsole prüfen
  - API-Endpunkt /health aufrufen

## 7. Implementierungsprotokoll (automatisch fortgeführt)
- 2026-04-16: Legacy-MVC Notenrechner analysiert (Quelle: upload/webprojekt.zip).
- 2026-04-16: Upload-Begleitdokumente schueler_max_korrekturhilfe_draft.md und schueler_max_korrekturhilfe_draft.html analysiert.
- 2026-04-16: Zielstruktur für Full-Stack-Template angelegt.
- 2026-04-16: FastAPI-Service inkl. OOP-Fachlogik, Validierung und Persistenz implementiert.
- 2026-04-16: Web-Frontend für Eingabe, Ergebnis und Historie implementiert.
- 2026-04-16: Docker Compose und Validierungsskripte eingerichtet.
- 2026-04-16: README- und Handbuch-Verlinkungen vorbereitet.
