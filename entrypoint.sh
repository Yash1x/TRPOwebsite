#!/bin/sh
set -eu

cd /app

# Wait for Postgres to accept connections
python - <<'PY'
import os, time
import psycopg2

host = os.getenv('POSTGRES_HOST', 'db')
port = int(os.getenv('POSTGRES_PORT', '5432'))
db   = os.getenv('POSTGRES_DB', 'trpo_portfolio')
user = os.getenv('POSTGRES_USER', 'trpo_user')
pw   = os.getenv('POSTGRES_PASSWORD', '')

deadline = time.time() + 60
while True:
    try:
        conn = psycopg2.connect(host=host, port=port, dbname=db, user=user, password=pw)
        conn.close()
        break
    except Exception as e:
        if time.time() > deadline:
            raise
        time.sleep(1)
PY

python manage.py migrate --noinput

# Optional: create static root if you ever add collectstatic
# python manage.py collectstatic --noinput

exec python manage.py runserver 0.0.0.0:8000
