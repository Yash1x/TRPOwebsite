# TRPOwebsite (Django + PostgreSQL)

## Функционал

- Главная страница с работами, сгруппированными по категориям.
- Страница работы с большим изображением, описанием и галереей.
- Страница «Услуги» со списком услуг и ценами.
- Страницы «О нас» и «Помощь».
- Авторизация (логин/логаут, регистрация пользователя).
- Добавление категорий и работ через веб-формы (для авторизованных сотрудников).
- Статика и медиа (превью и изображения работ).

## Локальный запуск без Docker (опционально)

1) Клонировать репозиторий:
```bash
git clone <URL>
cd TRPOwebsite-main
```

2) Создать и активировать venv:
```bash
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
# Windows CMD
.\.venv\Scripts\activate.bat
```

3) Установить зависимости:
```bash
pip install -r requirements.txt
```

4) Настроить доступ к PostgreSQL (см. `.env.example`) и выполнить миграции:
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Запуск через Docker (Django + Postgres)

### 1) Подготовка

- На компьютере, где будете показывать проект, должен быть установлен Docker (Docker Desktop на Windows/macOS или Docker Engine на Linux) и `docker compose`.
- В корне проекта есть пример переменных окружения `.env.example`. Для демо можно не создавать `.env` — в `docker-compose.yml` уже есть дефолты.

### 2) Запуск

В корне проекта:
```bash
docker compose up --build
```

После запуска сайт будет доступен:
- http://localhost:8000

### 3) Админка

Создать администратора:
```bash
docker compose exec web python manage.py createsuperuser
```

Админка:
- http://localhost:8000/admin/

### 4) Остановить
```bash
docker compose down
```

### 5) Полная очистка (включая БД)
Внимание: удалит данные Postgres.
```bash
docker compose down -v
```
