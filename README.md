# Task and Habit Tracker API

Полнофункциональный REST API для управления задачами и привычками с поддержкой аутентификации через JWT.

## 📋 Возможности

- ✅ Регистрация и вход пользователей
- ✅ JWT-базированная аутентификация
- ✅ Управление задачами (CRUD операции)
- ✅ Управление привычками с отслеживанием выполнения
- ✅ Безопасное хеширование паролей (Argon2)
- ✅ PostgreSQL база данных
- ✅ Миграции через Alembic

## 🛠️ Технологический стек

- **Backend Framework**: FastAPI 0.129.0
- **Web Server**: Uvicorn 0.40.0
- **Database**: PostgreSQL 15+
- **ORM**: SQLAlchemy 2.0.46
- **Authentication**: Python-Jose 3.5.0 + Passlib 1.7.4
- **Password Hashing**: Argon2
- **Validation**: Pydantic 2.12.5
- **Migrations**: Alembic 1.18.3+

## 📦 Требования

- Python 3.14+
- PostgreSQL 15+
- pip или другой менеджер пакетов Python

## 🚀 Установка

### 1. Клонирование репозитория

```bash
git clone <repository-url>
cd Task_and_Habit_Tracker_API
```

### 2. Создание виртуального окружения

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# или
venv\Scripts\activate  # Windows
```

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4. Конфигурация окружения

Скопируйте `.env.example` в `.env` и отредактируйте значения:

```bash
cp .env.example .env
```

**Переменные окружения:**
```env
DATABASE_URL=postgresql+psycopg2://postgres:postgres@localhost:5432/task_habit
JWT_SECRET_KEY=your-secret-key-here
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=60
```

### 5. Создание базы данных

```bash
psql -U postgres -c "CREATE DATABASE task_habit;"
```

### 6. Запуск миграций

```bash
alembic upgrade head
```

## 🏃 Запуск приложения

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Приложение будет доступно по адресу: `http://localhost:8000`

## 📚 API Документация

### Автоматическая интерактивная документация

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🔐 Endpoints аутентификации

### Регистрация
```http
POST /auth/register
Content-Type: application/json

{
  "email": "user@example.com",
  "username": "username",
  "password": "securepassword123"
}
```

**Ответ (201 Created):**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "user": {
    "id": 1,
    "email": "user@example.com",
    "username": "username",
    "is_active": true
  }
}
```

### Вход
```http
POST /auth/login
Content-Type: application/x-www-form-urlencoded

username=user@example.com&password=securepassword123
```

**Ответ (200 OK):**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

### Профиль пользователя
```http
GET /auth/profile
Authorization: Bearer <access_token>
```

**Ответ (200 OK):**
```json
{
  "id": 1,
  "email": "user@example.com",
  "username": "username",
  "is_active": true
}
```

### Проверка здоровья
```http
GET /health
```

**Ответ (200 OK):**
```json
{
  "status": "ok"
}
```

## 📊 Модели данных

### User
```
├── id (BigInteger) - Primary Key
├── email (String, 320) - Unique, Indexed
├── username (String, 50) - Unique, Indexed
├── hashed_password (String, 255)
├── is_active (Boolean) - Default: true
└── created_at (DateTime) - Auto-set
```

### Task
```
├── id (BigInteger) - Primary Key
├── user_id (BigInteger) - Foreign Key → User
├── title (String, 255) - Required
├── description (Text) - Optional
├── due_at (DateTime) - Optional, Indexed
├── is_completed (Boolean) - Default: false
├── created_at (DateTime) - Auto-set
└── updated_at (DateTime) - Auto-set
```

### Habit
```
├── id (BigInteger) - Primary Key
├── user_id (BigInteger) - Foreign Key → User
├── name (String, 255) - Required
├── description (Text) - Optional
├── frequency (String, 20) - Values: 'daily', 'weekly', 'monthly'
├── target_count (Integer) - Default: 1
├── created_at (DateTime) - Auto-set
└── updated_at (DateTime) - Auto-set
```

### HabitCompletion
```
├── id (BigInteger) - Primary Key
├── habit_id (BigInteger) - Foreign Key → Habit
├── completed_on (Date) - Required, Unique with habit_id
├── note (Text) - Optional
└── created_at (DateTime) - Auto-set
```

## 🗂️ Структура проекта

```
app/
├── main.py                 # Главное приложение FastAPI
├── api/                    # API endpoints (в разработке)
├── core/
│   ├── auth.py            # Функции аутентификации и JWT
│   ├── config.py          # Конфигурация переменных окружения
│   └── database.py        # Подключение к БД и сессии
├── models/                # SQLAlchemy модели
│   ├── user.py
│   ├── task.py
│   └── habit.py
├── schemas/               # Pydantic schemas для валидации
│   └── auth.py
├── services/              # Бизнес-логика (в разработке)
├── repositories/          # Слой доступа к данным (в разработке)
└── exceptions/            # Пользовательские исключения (в разработке)

alembic/                   # Миграции БД
├── env.py
└── versions/

.env                       # Переменные окружения (не коммитить)
.env.example              # Шаблон переменных окружения
requirements.txt          # Python зависимости
pyproject.toml           # Конфигурация проекта
```

## 🔧 Миграции БД

### Создание новой миграции
```bash
alembic revision --autogenerate -m "Описание изменений"
```

### Применение миграций
```bash
alembic upgrade head
```

### Откат последней миграции
```bash
alembic downgrade -1
```

## 🧪 Тестирование

Пока тесты не импортированы. Используйте Swagger UI для тестирования endpoints:

1. Откройте http://localhost:8000/docs
2. Нажмите "Try it out" для любого endpoint
3. Заполните необходимые поля
4. Нажмите "Execute"

## 🔒 Безопасность

- Пароли хешируются с помощью Argon2 (в зависимостях используется bcrypt из requirements.txt)
- JWT токены подписаны с помощью HS256
- Все пароли требуют минимум 8 символов
- Email валидируется с помощью Pydantic EmailStr
- CORS и дополнительная безопасность будут добавлены позже

## 📝 Лицензия

Этот проект лицензирован под лицензией MIT.

## 👤 Автор

Дастан/Никита

## 📞 Поддержка

Для вопросов и поддержки создавайте issues в репозитории.
