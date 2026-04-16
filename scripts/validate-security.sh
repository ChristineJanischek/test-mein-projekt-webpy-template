#!/usr/bin/env bash
set -euo pipefail

EXIT=0

search() {
  local pattern="$1"
  shift
  if command -v rg >/dev/null 2>&1; then
    rg -n "$pattern" "$@"
  else
    grep -RInE "$pattern" "$@"
  fi
}

echo "[security] Suche nach potenziellen Secrets..."
if search '(AKIA[0-9A-Z]{16}|BEGIN PRIVATE KEY|password\s*=\s*".+"|secret\s*=\s*".+")' \
  --exclude-dir=.git \
  --exclude-dir=upload \
  --exclude-dir=legacy-analysis/source \
  --exclude=validate-security.sh \
  .; then
  echo "[security] Warnung: mögliche Secret-Funde." >&2
  EXIT=1
else
  echo "[security] Keine offensichtlichen Secrets gefunden."
fi

echo "[security] Prüfe auf eval()-Nutzung in Python/PHP..."
if search 'eval\(' services webapp legacy-analysis/source/04_PHP; then
  echo "[security] Warnung: eval()-Aufrufe gefunden." >&2
  EXIT=1
else
  echo "[security] Keine eval()-Aufrufe gefunden."
fi

exit ${EXIT}
