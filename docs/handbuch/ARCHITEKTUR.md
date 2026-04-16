# Architektur

## Zielbild

Frontend (Nginx + statische Web-App)
-> API-Layer (FastAPI)
-> Service-Layer (GradeEvaluationService)
-> Data-Layer (MySQL via SQLAlchemy)

## Komponenten
- webapp/index.html:
  - Responsives UI, Eingabe und Darstellung.
- services/python-api/app/main.py:
  - REST-Endpunkte, Orchestrierung, Persistenz-Aufruf.
- services/python-api/app/services.py:
  - Fachlogik für Durchschnitt und Nachhilfebedarf.
- services/python-api/app/db.py:
  - ORM, Sessions, Tabellenmanagement.
- docker-compose.yml:
  - Betriebsumgebung für Web, API und Datenbank.

## Architekturprinzipien
- Separation of Concerns.
- Single Responsibility innerhalb der Python-Module.
- DRY durch zentrale Service-Logik.
- Erweiterbarkeit über zusätzliche Endpunkte und Services.

## Sicherheitsaspekte
- Schema-Validierung per Pydantic.
- HTML-Ausgabe ohne serverseitiges Template-Injection-Risiko.
- Security-Gates als Teil der Betriebsroutinen.
