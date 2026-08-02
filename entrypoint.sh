#!/bin/sh
set -e

echo "Menunggu database siap..."
python - <<'PYEOF'
import os, socket, time
host = os.environ.get("DB_HOST", "db")
port = int(os.environ.get("DB_PORT", "5432"))
for _ in range(30):
    try:
        socket.create_connection((host, port), timeout=2).close()
        break
    except OSError:
        time.sleep(1)
else:
    raise SystemExit("Database tidak bisa dijangkau, berhenti.")
PYEOF

echo "Menjalankan migrasi..."
python manage.py migrate --noinput

echo "Mengumpulkan static files..."
python manage.py collectstatic --noinput

echo "Menjalankan Gunicorn..."
exec gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 3
