#!/usr/bin/env bash
set -euo pipefail

echo "[start] Starte Services via Docker Compose..."
docker compose up -d --build

echo "[start] Verfügbar unter:"
echo "  Frontend: http://localhost:8000"
echo "  API:      http://localhost:5000/docs"
