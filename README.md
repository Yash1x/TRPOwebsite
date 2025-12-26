# TRPOwebsite — запуск проекта

## 1) Запуск через Docker

### Требования
- Docker + Docker Compose
- Git

### Шаги
```bash
git clone https://github.com/Yash1x/TRPOwebsite.git
cd TRPOwebsite

# создать .env из примера
cp .env.example .env  # macOS/Linux
# copy .env.example .env  # Windows PowerShell

# сборка и запуск
docker compose up --build
```

Сайт: http://localhost:8000

(Опционально, админ-пользователь)
```bash
docker compose exec web python manage.py createsuperuser
```

Админка: http://localhost:8000/admin


## 2) Запуск без Docker (локально)

### Требования
- Python 3.x
- PostgreSQL
- Git

### Шаги
```bash
git clone https://github.com/Yash1x/TRPOwebsite.git
cd TRPOwebsite

# виртуальное окружение
python -m venv .venv
# активация:
# Windows PowerShell: .\.venv\Scripts\Activate.ps1
# Windows CMD:        .\.venv\Scripts\activate.bat
# macOS/Linux:        source .venv/bin/activate

# зависимости
pip install -r requirements.txt

# создать .env из примера и указать доступы к локальному PostgreSQL
cp .env.example .env  # macOS/Linux
# copy .env.example .env  # Windows PowerShell

# миграции и запуск
python manage.py migrate
python manage.py runserver
```

Сайт: http://127.0.0.1:8000

```bash
python manage.py createsuperuser
```

Админка: http://127.0.0.1:8000/admin
