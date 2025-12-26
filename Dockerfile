# Simple dev-friendly image for Django + PostgreSQL
FROM python:3.12-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# System deps (Pillow, etc.)
# System deps (Pillow, psycopg2, etc.)
RUN set -eux; \
    # network tolerances
    printf 'Acquire::ForceIPv4 "true";\nAcquire::Retries "10";\nAcquire::http::Timeout "30";\nAcquire::https::Timeout "30";\n' > /etc/apt/apt.conf.d/99network; \
    \
    # rewrite apt sources to HTTPS + stable mirror
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
    \
    apt-get update; \
    apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
        libjpeg62-turbo-dev \
        zlib1g-dev \
        libpng-dev \
        ca-certificates \
    ; \
    rm -rf /var/lib/apt/lists/*



# Install Python deps
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip \
    && pip install -r /app/requirements.txt

# Copy project
COPY . /app

# Copy and mark entrypoint executable
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]
