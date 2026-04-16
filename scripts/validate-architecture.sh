#!/usr/bin/env bash
set -euo pipefail

REQUIRED_PATHS=(
  "services/python-api/app/main.py"
  "services/python-api/app/services.py"
  "webapp/index.html"
  "docker-compose.yml"
  "docs/handbuch/PFLICHTENHEFT.md"
  "docs/handbuch/HANDBUCH.md"
)

echo "[arch] Prüfe erforderliche Architekturdateien..."
for path in "${REQUIRED_PATHS[@]}"; do
  if [[ ! -f "$path" ]]; then
    echo "[arch] Fehlt: $path" >&2
    exit 1
  fi
  echo "[arch] OK: $path"
done

echo "[arch] Architekturprüfung erfolgreich."
