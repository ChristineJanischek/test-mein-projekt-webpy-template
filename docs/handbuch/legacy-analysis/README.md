# Legacy-Analyse

## Quelle
- Upload-Archiv: upload/webprojekt.zip
- Entpackter Quellstand: legacy-analysis/source/04_PHP
- Bewertungsentwurf (Markdown): upload/schueler_max_korrekturhilfe_draft.md
- Bewertungsentwurf (HTML): upload/schueler_max_korrekturhilfe_draft.html

## Ist-Analyse
- MVC-Struktur in PHP vorhanden (Model, View, Controller).
- Fachlogik korrekt für Notendurchschnitt und Nachhilfebedarf.
- Eingabevalidierung vorhanden.
- Keine persistente Speicherung von Ergebnissen.
- Kein containerisierter Betrieb.
- Draft-Dokumente zeigen didaktische Qualitätskriterien (Struktur, Design, Doku, Formales), die als Zusatzanforderungen in Wartbarkeit und Nachvollziehbarkeit eingeflossen sind.

## Übernahmeentscheidungen
- Fachregel unverändert übernommen:
  - Durchschnitt über vier Fächer.
  - Nachhilfe bei Note > 4.0.
- Präsentationslogik in ein modernes statisches Web-Frontend überführt.
- Controller-/Model-Gedanke in API + Service-Layer übertragen.
- Persistenzschicht mit MySQL ergänzt.

## Migrationsartefakte
- Legacy-Quelle bleibt nachvollziehbar in legacy-analysis/source.
- Zielimplementierung liegt in services/python-api und webapp.
