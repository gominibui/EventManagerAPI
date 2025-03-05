# Event Management API

## Опис проекта / Project Description

Це API для управління подіями, створене за допомогою Django та Django REST Framework. API дозволяє користувачам створювати, переглядати, оновлювати та видаляти події, а також реєструвати користувачів на ці події. Використовується система автентифікації JWT для захисту користувацьких даних та доступу до подій.

This is an Event Management API built with Django and Django REST Framework. The API allows users to create, view, update, delete events, and register users for these events. It uses JWT authentication to secure user data and access to events.

## Основні функції / Key Features

- CRUD операції для управління подіями (Create, Read, Update, Delete).
- Реєстрація та автентифікація користувачів за допомогою JWT.
- Організатор події автоматично визначається як користувач, що створив подію.
- Документація API за допомогою `drf_spectacular` та Swagger.
- Фільтрація подій за датою та місцем.
- Підтримка Docker і Docker Compose для зручного запуску проекту.

## Технології / Technologies

- **Django** — основний фреймворк.
- **Django REST Framework** — для створення API.
- **drf_spectacular** — для автоматичного генерування документації API.
- **SQLite** — база даних (можна замінити на PostgreSQL, MySQL тощо).
- **Docker** — для контейнеризації додатку.
- **Docker Compose** — для керування декількома контейнерами (сервер та база даних).
- **JWT Authentication** — для автентифікації користувачів.

## Установка / Installation

### 1. Клонуйте репозиторій / Clone the repository

```bash
git clone https://github.com/gominibui/EventManagerAPI.git
cd EventManagerAPI
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
docker build -t eventmanagerapi .
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
  "location": "Kyiv, Ukraine"
}
```

**Примітка:** Організатор події автоматично ставиться на основі користувача, який створив подію.

### 2. Отримання списку подій / Get event list

**GET** `/api/events/`

### 3. Отримання події за ID / Get event by ID

**GET** `/api/events/{id}/`

### 4. Оновлення події / Update an event

**PATCH** `/api/events/{id}/`

Тіло запиту:

```json
{
  "description": "Updated description for the conference."
}
```

### 5. Видалення події / Delete an event

**DELETE** `/api/events/{id}/`

Цей запит додасть користувача до події як учасника.

### 7. Фільтрація подій / Filter events

**GET** `/api/events/?date_after=2025-01-01&location=Kyiv`

Цей запит поверне всі події після 1 січня 2025 року в Києві. Ви можете використовувати різні параметри для фільтрації за датою, місцем та іншими критеріями.

## Ліцензія / License

MIT License

## Автори / Authors

- Gominibui - Lead Developer
- [GitHub Profile](https://github.com/gominibui)
```
