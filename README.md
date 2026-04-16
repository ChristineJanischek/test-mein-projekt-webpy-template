# Test Mein Projekt WebPy Template

Produktionsnahe Full-Stack-Vorlage mit dokumentierter Legacy-Analyse, API-Service, Web-Frontend, Persistenz und Quality-Gates.

## Ausgangsbasis
- Quellcode-Quelle für die Migration: [upload/webprojekt.zip](upload/webprojekt.zip)
- Entpackte Analysebasis: [legacy-analysis/source](legacy-analysis/source)

## Schnellstart
1. Voraussetzungen prüfen:
	- `bash scripts/bootstrap.sh`
2. Services starten:
	- `bash scripts/start-services.sh`
3. Anwendungen öffnen:
	- Frontend: `http://localhost:8000`
	- API-Dokumentation: `http://localhost:5000/docs`

## Architekturüberblick
- Frontend: [webapp/index.html](webapp/index.html)
- API: [services/python-api/app/main.py](services/python-api/app/main.py)
- Business-Logik: [services/python-api/app/services.py](services/python-api/app/services.py)
- Persistenz: [services/python-api/app/db.py](services/python-api/app/db.py)
- Orchestrierung: [docker-compose.yml](docker-compose.yml)

## Dokumentation
- Pflichtenheft: [docs/handbuch/PFLICHTENHEFT.md](docs/handbuch/PFLICHTENHEFT.md)
- Handbuch: [docs/handbuch/HANDBUCH.md](docs/handbuch/HANDBUCH.md)
- Architektur: [docs/handbuch/ARCHITEKTUR.md](docs/handbuch/ARCHITEKTUR.md)
- Dokumentationsindex: [docs/handbuch/INDEX.md](docs/handbuch/INDEX.md)
- Legacy-Analyse: [docs/handbuch/legacy-analysis/README.md](docs/handbuch/legacy-analysis/README.md)

## Quality Gates
- `bash scripts/validate-security.sh`
- `bash scripts/validate-architecture.sh`
- `bash scripts/validate-docs.sh`

## Entwicklungsstruktur
```
.
├── docs/handbuch/
├── legacy-analysis/
├── services/python-api/
├── webapp/
├── scripts/
└── docker-compose.yml
```
