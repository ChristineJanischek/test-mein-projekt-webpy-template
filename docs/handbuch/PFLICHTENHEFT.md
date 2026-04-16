# Pflichtenheft

## 1. Ausgangslage
- Ausgangsquelle ist die Datei upload/webprojekt.zip.
- Enthaltener Legacy-Stand: PHP-MVC Notenrechner mit Fächern BWL, Mathe, Deutsch, Englisch und Nachhilfe-Logik (> 4.0).
- Ziel: produktionsnahe, wartbare WebPy-Template-Struktur mit dokumentierter Architektur und Automation.

## 2. Muss-Anforderungen
- Webbasierte Anwendung mit responsiver Oberfläche.
- Trennung von Präsentation, Steuerung und Fachlogik (MVC-orientiert).
- Persistenzschicht für Rechenergebnisse.
- Sicherheits-Basismaßnahmen (Input-Validierung, keine ungefilterte Ausgabe).
- Dokumentation: Pflichtenheft, Handbuch, Architektur, Legacy-Analyse.
- Automatisierte Prüfskripte für Security-, Architektur- und Dokumentations-Gates.
- Containerisierte Ausführung via Docker Compose.

## 3. Umgesetzte Anforderungen
- Frontend: webapp/index.html als responsive Oberfläche.
- API-Layer: FastAPI unter services/python-api/app/main.py.
- Service-Layer: OOP-Fachlogik in services/python-api/app/services.py.
- Data-Layer: MySQL + SQLAlchemy in services/python-api/app/db.py.
- Automatisierung: scripts/bootstrap.sh, scripts/start-services.sh, scripts/validate-*.sh.
- Dokumentation: docs/handbuch/* inklusive Legacy-Analyse.

## 4. Nicht-funktionale Anforderungen
- Wartbarkeit durch modulare Struktur.
- Erweiterbarkeit durch klar getrennte Schichten.
- Nachvollziehbarkeit durch Änderungsprotokoll in Handbuch und Pflichtenheft.
- Betriebsfähigkeit lokal über docker compose.

## 5. Abnahmekriterien
- docker compose up -d --build startet Frontend, API und MySQL.
- Frontend kann Noten an API senden und Ergebnis anzeigen.
- Ergebnisse werden in MySQL gespeichert und über API-Historie abrufbar.
- validate-security.sh, validate-architecture.sh, validate-docs.sh laufen erfolgreich.

## 6. Änderungsprotokoll (automatisch fortgeführt)
- 2026-04-16: Legacy-ZIP in legacy-analysis/source entpackt und analysiert.
- 2026-04-16: Upload-Draft-Dateien (HTML/Markdown Korrekturhilfe) analysiert und als Qualitätskontext dokumentiert.
- 2026-04-16: Zielarchitektur mit API, Persistenz, Frontend und Docker Compose implementiert.
- 2026-04-16: Dokumentationssatz (Pflichtenheft, Handbuch, Architektur, Legacy-Analyse) erstellt.
