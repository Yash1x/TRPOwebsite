import os
import time
import psycopg2

host = os.getenv("POSTGRES_HOST", "db")
port = int(os.getenv("POSTGRES_PORT", "5432"))
db = os.getenv("POSTGRES_DB", "trpo_portfolio")
user = os.getenv("POSTGRES_USER", "trpo_user")
password = os.getenv("POSTGRES_PASSWORD", "trpo_pass")

deadline = time.time() + 60  # seconds
last_err = None

while time.time() < deadline:
    try:
        conn = psycopg2.connect(
            host=host,
            port=port,
            dbname=db,
            user=user,
            password=password,
        )
        conn.close()
        print("Postgres is ready.")
        raise SystemExit(0)
    except Exception as e:
        last_err = e
        print(f"Waiting for Postgres at {host}:{port}... ({e})")
        time.sleep(2)

raise SystemExit(f"Postgres not ready in time. Last error: {last_err}")
