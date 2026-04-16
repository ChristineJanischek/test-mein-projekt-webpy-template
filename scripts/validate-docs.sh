#!/usr/bin/env bash
set -euo pipefail

DOCS=(
  "docs/handbuch/INDEX.md"
  "docs/handbuch/README.md"
  "docs/handbuch/PFLICHTENHEFT.md"
  "docs/handbuch/HANDBUCH.md"
  "docs/handbuch/ARCHITEKTUR.md"
  "docs/handbuch/legacy-analysis/README.md"
)

echo "[docs] Prüfe Dokumentationsdateien..."
for doc in "${DOCS[@]}"; do
  if [[ ! -f "$doc" ]]; then
    echo "[docs] Fehlt: $doc" >&2
    exit 1
  fi
  echo "[docs] OK: $doc"
done

echo "[docs] Dokumentationsprüfung erfolgreich."
