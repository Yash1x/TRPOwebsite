# Simple dev-friendly image for Django + PostgreSQL
FROM python:3.12-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Достаточно только runtime-зависимостей (без build-essential)
# libpq5 нужен для psycopg2, libjpeg/libpng/zlib обычно не нужны если Pillow ставится wheel'ом,
# но оставим минимально безопасный набор.
RUN set -eux; \
    printf 'Acquire::ForceIPv4 "true";\nAcquire::Retries "10";\nAcquire::http::Timeout "30";\nAcquire::https::Timeout "30";\n' > /etc/apt/apt.conf.d/99network; \
    if [ -f /etc/apt/sources.list.d/debian.sources ]; then \
      sed -i 's|http://deb.debian.org|https://mirror.yandex.ru|g' /etc/apt/sources.list.d/debian.sources; \
      sed -i 's|http://security.debian.org|https://mirror.yandex.ru|g' /etc/apt/sources.list.d/debian.sources; \
      sed -i 's|https://deb.debian.org|https://mirror.yandex.ru|g' /etc/apt/sources.list.d/debian.sources; \
      sed -i 's|https://security.debian.org|https://mirror.yandex.ru|g' /etc/apt/sources.list.d/debian.sources; \
    else \
      sed -i 's|http://deb.debian.org|https://mirror.yandex.ru|g' /etc/apt/sources.list; \
      sed -i 's|http://security.debian.org|https://mirror.yandex.ru|g' /etc/apt/sources.list; \
      sed -i 's|https://deb.debian.org|https://mirror.yandex.ru|g' /etc/apt/sources.list; \
      sed -i 's|https://security.debian.org|https://mirror.yandex.ru|g' /etc/apt/sources.list; \
    fi; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
        ca-certificates \
        libpq5 \
    ; \
    rm -rf /var/lib/apt/lists/*

# Python deps
COPY requirements.txt /app/requirements.txt

ENV PIP_DEFAULT_TIMEOUT=300 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

# ВАЖНО: не обновляем pip, не тянем /simple/pip/
RUN python -m pip install --retries 15 --timeout 300 --prefer-binary -r /app/requirements.txt

# Project
COPY . /app

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 8000
ENTRYPOINT ["/entrypoint.sh"]
