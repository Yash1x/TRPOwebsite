# TRPOwebsite (Django + PostgreSQL)

## Функционал

- Главная страница с работами, сгруппированными по категориям.
- Страница работы с большим изображением, описанием и галереей.
- Страница «Услуги» со списком услуг и ценами.
- Страницы «О нас» и «Помощь».
- Авторизация (логин/логаут, регистрация пользователя).
- Добавление категорий и работ через веб-формы (для авторизованных сотрудников).
- Статика и медиа (превью и изображения работ).

## Локальный запуск без Docker

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

Перед запуском на компьютере должны быть установлены:

- **Docker Desktop** (Windows/macOS) или **Docker Engine + Docker Compose** (Linux)
- **Git** (желательно, чтобы клонировать репозиторий)

Проверка в терминале / PowerShell:

```bash
docker --version
docker compose version
git --version
```
2) Как скачать проект
Вариант A (рекомендуется): через Git
```bash
git clone https://github.com/Yash1x/TRPOwebsite.git
cd TRPOwebsite
```
Вариант B: скачать ZIP
На GitHub нажмите Code → Download ZIP

Распакуйте архив

Откройте терминал в папке проекта (там, где лежит docker-compose.yml)

3) Подготовка файла .env
В проекте есть пример настроек: .env.example.
Его нужно скопировать в .env.

Windows (PowerShell)
powershell
```copy .env.example .env```
macOS/Linux
bash
```cp .env.example .env```
Откройте .env и проверьте, что там есть настройки Django и PostgreSQL.
Важно: в Docker-режиме POSTGRES_HOST должен быть равен db (это имя сервиса PostgreSQL в docker-compose.yml), а не localhost.

4) Запуск через Docker
Запуск (сборка + старт контейнеров):

```bash
docker compose up --build
```
После успешного запуска сайт будет доступен по адресу:

http://localhost:8000

Остановить проект:

Ctrl + C в терминале

Запуск в фоне (чтобы терминал был свободен):

```bash
docker compose up -d --build
```
Остановить контейнеры:

```bash
docker compose down
```
5) Миграции (создание таблиц в PostgreSQL)
В большинстве случаев миграции выполняются автоматически при старте контейнера web.
Если в логах есть ошибки про отсутствие таблиц (например, auth_user) — выполните миграции вручную:

```bash
docker compose exec web python manage.py migrate
```
6) Создание администратора (для входа в админку Django)
Чтобы создать учётную запись администратора:

```bash
docker compose exec web python manage.py createsuperuser
```
Админка Django:

http://localhost:8000/admin

7) Проверка PostgreSQL (без установки psql на компьютер)
Можно зайти в PostgreSQL прямо внутри контейнера:

```bash
docker compose exec db psql -U $POSTGRES_USER -d $POSTGRES_DB
```
Полезные команды внутри psql:

```sql
\dt
SELECT * FROM django_migrations ORDER BY applied DESC LIMIT 10;
\q
```
8) Типовые проблемы и решения
Проблема: порт 5432 занят
Если на компьютере уже установлен PostgreSQL, Docker может не поднять контейнер из-за занятого порта.

Решения:

остановить локальный PostgreSQL

или изменить проброс порта в docker-compose.yml (например на 5433:5432)

или убрать проброс порта db наружу, если он не нужен

Проблема: relation "auth_user" does not exist
Это значит, что миграции не применились. Выполните:

```bash
docker compose exec web python manage.py migrate
```
Проблема: сайт не открывается, хотя контейнеры запущены
Проверьте контейнеры:

```bash
docker compose ps
```
Посмотрите логи:

```bash
docker compose logs web
docker compose logs db
```
9) Полный сброс базы данных (начать “с нуля”)
⚠️ Внимание: команда ниже удалит данные PostgreSQL (volume).

```bash
docker compose down -v
docker compose up --build
```
10) Быстрый запуск (самая короткая памятка)
```bash
git clone https://github.com/Yash1x/TRPOwebsite.git
cd TRPOwebsite
cp .env.example .env   # Windows: copy .env.example .env
docker compose up -d --build
docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
```
Сайт: http://localhost:8000
Админка: http://localhost:8000/admin
