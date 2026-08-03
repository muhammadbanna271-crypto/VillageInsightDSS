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
# --timeout dinaikkan dari default 30 detik: proses bulk import
# (ribuan Response.objects.update_or_create satu per satu) untuk
# 1.152 responden x 88 indikator bisa lebih lama dari itu, apalagi
# bicara ke PostgreSQL di container terpisah (bukan SQLite lokal).
exec gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 3 --timeout 600
