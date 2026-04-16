#!/usr/bin/env bash
set -euo pipefail

echo "[bootstrap] Prüfe Docker-Verfügbarkeit..."
if ! command -v docker >/dev/null 2>&1; then
  echo "[bootstrap] Fehler: docker ist nicht installiert." >&2
  exit 1
fi

if ! docker compose version >/dev/null 2>&1; then
  echo "[bootstrap] Fehler: docker compose ist nicht verfügbar." >&2
  exit 1
fi

echo "[bootstrap] Basisprüfung abgeschlossen."
