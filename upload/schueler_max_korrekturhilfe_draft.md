# Korrekturhilfe (Draft)

Projekt: schueler_nikita
Rubrik: webprojekte
Punkte: 34.50 / 36.00
Note: 1.21

## Kriterien

- [teilweise] A1: Formales – Syntax, MVC, kein Rechner/Automat, Abgabe (2.50/4.00)
  Evidenz: PHP-CLI nicht verfuegbar, MVC-Ordner vorhanden: controllers, models, views, Dynamik-Hinweis in views/RechnerView.php
  Hinweis: Syntaxcheck nicht ausfuehrbar (php nicht installiert), neutral bewertet. | MVC-Konzept angewendet. | Dynamischer Teil (Rechner/Automat) erkannt. | Abgabe 20 Minuten verspaetet (milde bewertet). | Vier Teilprüfungen werden automatisch dokumentiert; Sonderregel zur milden Verspätung ist hinterlegt.
- [erfuellt] B1: Projektstruktur und Quellcode-Qualität (4.00/4.00)
  Evidenz: index.php, css/styles.css, css/rechner.css
  Hinweis: 3/3 Teilregeln erfüllt | Einrückung, relative PHP-Pfade (require __DIR__) und Effizienz manuell prüfen.
- [erfuellt] C1: Dynamisches Layout und Inhalt (4.00/4.00)
  Evidenz: index.php, pages/haftung.php, pages/impressum.php
  Hinweis: 3/3 Teilregeln erfüllt | Box-Modell-Umsetzung und Browserkompatibilität manuell prüfen.
- [erfuellt] D1: Bilder und Galerie (4.00/4.00)
  Evidenz: images/rally1.jpg, images/moto1.jpg, images/Logo.png
  Hinweis: 3/3 Teilregeln erfüllt | Bildoptimierung (<200 KB je Bild), Bedienbarkeit von Preview/View im Browser und Verlinkung externer Quellen manuell pruefen.
- [erfuellt] E1: Verweise – interne und externe Links (4.00/4.00)
  Evidenz: layouts/header.php, layouts/main.php, layouts/footer.php
  Hinweis: 2/2 Teilregeln erfüllt | Qualität und Sinnhaftigkeit der Navigation manuell prüfen.
- [erfuellt] F1: PHP-Eigenanteil und Formulare (4.00/4.00)
  Evidenz: index.php, views/RechnerView.php, models/RechnerModel.php
  Hinweis: 2/2 Teilregeln erfüllt | Ideenreichtum, Eigenleistung und PHP-Qualität jenseits der Mindestanforderung manuell bewerten.
- [erfuellt] H1: Dokumentation aller Inhalte und Quellcodes (4.00/4.00)
  Evidenz: css/styles.css, css/rechner.css
  Hinweis: CSS-Kommentare vorhanden | Qualität und Vollständigkeit der Kommentierung manuell prüfen.
- [erfuellt] I1: Farbgestaltung und Design (4.00/4.00)
  Evidenz: css/styles.css, css/rechner.css, css/styles.css
  Hinweis: 6/6 Teilregeln erfüllt | Gesamteindruck, gestalterische Konsistenz und tatsaechliche responsive Wirkung im Browser manuell pruefen.
- [erfuellt] J1: Sonstige Features – Impressum, Datenschutz und KI-Inhalte (4.00/4.00)
  Evidenz: pages/impressum.php, pages/datenschutz.php, pages/haftung.php
  Hinweis: 3/3 Teilregeln erfüllt | Vollstaendigkeit von Impressum/Datenschutz, KI-Zitationen und Bildquellen/Lizenzen inhaltlich manuell pruefen.

## Zusammenfassung

Profil-basierte Erst-Korrekturhilfe 'Web-Projekt Oberstufe 2026'. 0 von 9 Kriterien erfordern manuelle Prüfung. Vorläufige Punkte bei ERFUELLT auf der 4/3/2/1-Skala anpassen.

## Marschplan: Vertiefung bis Anfang Juni

Zeige in der Verteidigung Anfang Juni, dass du dein Projekt nicht nur abgegeben, sondern weiterentwickelt hast. Zwei klar abgegrenzte Erweiterungen, gut dokumentiert und im Browser demonstrierbar, sind das Ziel.

### Erweiterung 1: Versionsverwaltung mit Git und GitHub

Git gehoert heute zum Handwerkszeug jeder Webentwicklerin. Ein sauberes GitHub-Repository mit nachvollziehbaren Commits zeigt in der Verteidigung, dass du professionell und strukturiert arbeitest. Das Thema ist gut in Eigenregie erlernbar und der Aufwand ist klar begrenzt.

**Aufwand und Schritte:** Zeitaufwand: ca. 3 Abende. Schritte: (1) GitHub-Account und oeffentliches Repository anlegen, (2) Projekt mit 'git init' initialisieren und in regelmaessigen Commits den Fortschritt dokumentieren, (3) einen Feature-Branch ('erweiterung-formular' o.ae.) erstellen, bearbeiten und mergen, (4) README.md mit Projektbeschreibung, Screenshot und Laufzeitanleitung ergaenzen. Dokumentation: Je Commit erklaeren, was geaendert wurde und warum.

### Erweiterung 2: KI-API-Integration: Grundlagen Machine Learning in der Praxis

Da dein Projekt bereits fundiert umgesetzt ist, bietet sich ein Blick in aktuelle KI-Werkzeuge an. Das Einbinden einer einfachen KI-API (z.B. OpenAI-Text-API, HuggingFace oder eine Bildklassifikation) zeigt technologische Offenheit und ist ein starkes Argument in der Verteidigung. Du musst kein ML-Modell trainieren – das Verstehen und Einbinden einer API reicht vollstaendig.

**Aufwand und Schritte:** Zeitaufwand: ca. 4-5 Abende. Schritte: (1) Kostenlosen API-Key bei OpenAI oder HuggingFace anlegen, (2) einfachen PHP-curl-Aufruf zur API bauen (z.B. Textzusammenfassung oder Bildanalyse), (3) Ergebnis sauber im Browser anzeigen und Fehlerbehandlung einbauen, (4) API-Key in einer .env-Datei oder Config-Datei sicher auslagern (nicht im HTML). Dokumentation: Welche API, welche Eingabe, welche Ausgabe, Screenshot des Ergebnisses.

### ToDo-Liste

- Woche 1-2: Git-Repository anlegen, Projekt einpflegen, ersten Feature-Branch erstellen.
- Parallel: Kriterium 'Formales – Syntax, MVC, kein Rechner/Automat, Abgabe' gezielt nacharbeiten – das staerkt die Gesamtbewertung.
- Woche 2-3: Erweiterungsthema 'KI-API-Integration: Grundlagen Machine Learning in der Praxis' recherchieren und Umsetzungsplan notieren.
- Woche 3-5: Erweiterung 'KI-API-Integration: Grundlagen Machine Learning in der Praxis' implementieren und Schritt fuer Schritt dokumentieren.
- Woche 5-6: Beide Erweiterungen im Browser demonstrieren und fuer die Verteidigung aufbereiten.
- Woche 6: Kurzes Verteidigungsskript erstellen: Was hast du getan, was hast du gelernt, was wuerdest du anders machen?

