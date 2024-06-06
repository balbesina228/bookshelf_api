# Bookshelf

## Description

This is a FastAPI-based project that implements an authentication and authorization system using JWT and cookies. The
project includes CRUD operations for managing "Book" and "Author" entities.

## Tech Stack

- **FastAPI**
- **PostgreSQL**
- **SQLAlchemy**
- **Pydantic**
- **Uvicorn**
- **Docker**
- **Docker Compose**

## Installation

1. **Clone the repository:**

    ```
    git clone https://github.com/balbesina228/bookshelf_api.git
    ```

2. **Create and activate a virtual environment:**

    ```
    python -m venv venv
    ```

    - Windows:
    ```
    .\venv\Scripts\activate
    ```
    - bash:
    ```
    source venv/bin/activate
    ```

3. **Install dependencies:**

    ```
    pip install -r reqs.txt
    ```

4. **Create and configure the `.env` file:**

   Create a copy of `env.example` to a file named `.env` in the root directory of the project.

## Running the Project

### Using Docker

1. **Build and start the containers:**

    ```
    docker-compose up --build
    ```

2. **The application will be available at:**

    ```
    http://localhost:8000/docs
    ```

### Manually (without Docker)

1. **Create database:**

    - run PostgreSQL shell
    - run `CREATE DATABASE db_bookshelf;`

2. **Apply database migrations:**

    ```
    alembic upgrade head
    ```

3. **Start the FastAPI application:**

    ```
    uvicorn src.main:app --host 0.0.0.0 --port 8000
    ```

4. **The application will be available at:**

    ```
    http://localhost:8000/docs
    ```