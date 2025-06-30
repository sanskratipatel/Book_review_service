# Book Review Service

A FastAPI-based web service for managing and reviewing books. It provides APIs for authentication, adding/listing books, and adding/viewing reviews. The app uses SQLite as the database, Redis for caching, and Pytest for automated testing.

---

## Features

* User signup and login with JWT authentication
* CRUD operations on Books and Reviews
* Redis-based caching for book listing
* SQLite as default database using SQLAlchemy ORM
* Automated testing using Pytest
* Configuration management with `.env` file

---

## Folder Structure

```
Book_review_service/
├── app/
│   ├── main.py                # Initializes FastAPI app and routers
│   ├── api/
│   │   ├── routes.py          # All route registrations
│   │   └── auth.py            # Authentication endpoints
│   ├── crud/
│   │   ├── books.py           # Logic for creating and reading books
│   │   └── review.py          # Logic for adding and retrieving reviews
│   ├── db/
│   │   ├── database.py        # DB engine and session setup
│   │   └── redis_cache.py     # Functions to cache book data in Redis
│   ├── models/
│   │   ├── book.py            # SQLAlchemy model for Book
│   │   |── review.py          # SQLAlchemy model for Review
|   |   |---user.py            # SQLAlchemy model for User
│   ├── schemas/
│   │   ├── book.py            # Pydantic validation schema for Book
│   │   └── review.py          # Pydantic schema for Review
|   |   |---user.py            # Pydantic schema for user
│   ├── core/
│   │   └── security.py        # JWT generation and password hashing
│   └── tests/
│       ├── test_auth.py       # Auth route test cases
│       ├── test_books.py      # Book route test cases
│       └── test_reviews.py    # Review route test cases
├── .env                       # Sensitive configuration
├── .gitignore                 # Files/directories to ignore in Git
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

---

## Why Each Module is Used

* **FastAPI**: Web framework for building high-performance APIs.
* **SQLAlchemy**: ORM to define models and interact with SQLite database using Python.
* **SQLite**: Lightweight database for local development and testing.
* **Pydantic**: For data validation and serialization using Python types.
* **Redis**: In-memory store to cache book lists and reduce DB calls.
* **Pytest**: Framework for writing unit tests.
* **python-dotenv**: Loads environment variables from `.env` file.
* **bcrypt / passlib**: Secure password hashing for storing passwords.
* **python-jose**: JWT creation and decoding for secure user authentication.

---

## Database Tables

### books

| Column      | Type | Description             |
| ----------- | ---- | ----------------------- |
| id          | int  | Primary key             |
| title       | str  | Title of the book       |
| author      | str  | Author of the book      |
| description | str  | Description of the book |

### reviews

| Column   | Type | Description                   |
| -------- | ---- | ----------------------------- |
| id       | int  | Primary key                   |
| content  | str  | Review content                |
| rating   | int  | Rating out of 5               |
| book\_id | int  | Foreign key referencing books |

---

## API Endpoints

### Auth Routes

* `POST /auth/signup`: Register a new user
* `POST /auth/token`: Log in and get JWT access token

### Book Routes

* `GET /books`: Get all books (uses Redis cache)
* `POST /books`: Add a new book (auth required)

### Review Routes

* `GET /books/{book_id}/reviews`: Get all reviews for a book (auth required)
* `POST /books/{book_id}/reviews`: Add a review to a book (auth required)

Note: All routes except `/auth/*` require a valid JWT token in the `Authorization` header.

---

## Environment Variables (`.env`)

```
DATABASE_URL=sqlite:///./books.db
REDIS_URL=redis://localhost 
SECRET_KEY=your-secret-key-generated
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

```

---

## Setup Instructions

### 1. Clone the repository and set up a virtual environment

```bash
git clone https://github.com/sanskratipatel/Book_review_service.git
python3 -m venv venv
source venv/bin/activate  # This is for Linux / WSL to activate Virtual Enviroment
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create SQLite tables

```bash
python
>>> from app.db.database import Base, engine
>>> Base.metadata.create_all(bind=engine)
>>> exit()
```

### 4. Start Redis (Linux/Mac)

```bash
sudo service redis-server start
# or
redis-server
```

> **Note for Windows**: Redis is not officially supported on Windows. Use WSL or Linux :

```bash
# WSL (Ubuntu) or Linux
sudo apt update
sudo apt install redis-server
sudo service redis-server start

---

## Run the Server

```bash
uvicorn app.main:app --reload   // For Start Fast Api Server 
```

Server will be available at:
`http://127.0.0.1:8000`
`http://127.0.0.1:8000/docs`  :- For Swagger
 OnSwagger if you click on  /openapi.json 
 You can see all routes Details  
 
---

## Run Tests

```bash
pytest -v
```

This runs all test cases in `app/tests/`.

-----
## Development Notes

* All API actions that require authentication must include a `Bearer` token in the `Authorization` header.
* Redis caching helps improve performance by storing book list responses for quick access.
* Pytest ensures all routes and logic are covered with unit tests.
* You can extend the system to support pagination, search, ratings average, and user roles. 

For More Details Contact :- patelsanskrati05@gmail.com 

---

