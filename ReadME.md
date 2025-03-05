```
# Event Management API

## Описание проекту / Project Description

Це API для управління подіями, створене за допомогою Django та Django REST Framework. API дозволяє створювати, переглядати, оновлювати та видаляти події, а також реєструвати користувачів на події.

This is an Event Management API built with Django and Django REST Framework. The API allows users to create, view, update, delete events, and register users for events.

## Основні функції / Key Features

- CRUD операції для управління подіями (Create, Read, Update, Delete).
- Реєстрація та автентифікація користувачів.
- Документація API з використанням `drf_spectacular` та Swagger.

## Технології / Technologies

- **Django** — основний фреймворк.
- **Django REST Framework** — для створення API.
- **drf_spectacular** — для автоматичного генерування документації API.
- **SQLite** — база даних (якщо використовується).
- **Docker** — контейнеризація додатку.
- **Docker Compose** — для керування декількома контейнерами (наприклад, сервером та базою даних).

## Установка / Installation

### 1. Клонуйте репозиторій / Clone the repository

```bash
git clone https://github.com/yourusername/EventManage.git
cd EventManage
```

### 2. Створіть та активуйте віртуальне середовище / Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # Для Linux/macOS
.venv\Scripts\activate  # Для Windows
```

### 3. Встановіть залежності / Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Виконайте міграції / Run migrations

```bash
python manage.py migrate
```

### 5. Створіть суперкористувача для доступу до адмінки / Create a superuser for admin access

```bash
python manage.py createsuperuser
```

### 6. Запустіть сервер / Run the server

```bash
python manage.py runserver
```

Тепер ви можете відкрити [http://127.0.0.1:8000](http://127.0.0.1:8000) у вашому браузері.

### 7. Для роботи з Docker / For Docker

1. Створіть образ Docker / Build the Docker image:

```bash
docker build -t eventmanage .
```

2. Запустіть Docker контейнер / Run the Docker container:

```bash
docker-compose up --build
```

Це створить і запустить сервер разом із базою даних у контейнерах Docker. 

### 8. Перевірка API / Checking the API

- **Документація API** доступна за адресою [http://127.0.0.1:8000/docs/](http://127.0.0.1:8000/docs/).
- **Адмінка** доступна за адресою [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) (потрібно увійти за допомогою створеного суперкористувача).

## Використання API / API Usage

### 1. Створення події / Create an event

**POST** `/api/events/`

Тіло запиту:

```json
{
  "title": "Conference 2025",
  "description": "Annual conference about tech innovations.",
  "date": "2025-05-01T10:00:00Z",
  "location": "Kyiv, Ukraine",
  "organizer": 1  # ID організатора (користувача)
}
```

### 2. Отримання списку подій / Get event list

**GET** `/api/events/`

### 3. Оновлення події / Update an event

**PATCH** `/api/events/{id}/`

Тіло запиту:

```json
{
  "description": "Updated description for the conference."
}
```

### 4. Видалення події / Delete an event

**DELETE** `/api/events/{id}/`

### 5. Реєстрація користувача на подію / Register a user for an event

**POST** `/api/events/{id}/register/`

Тіло запиту:

```json
{
  "user": 1  # ID користувача, який реєструється
}
```

## Ліцензія / License

MIT License

