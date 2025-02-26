# 🚀 FastAPI Project Setup Guide

This guide provides all the necessary **dependencies**, **virtual environment setup**, and **terminal commands** required to get the FastAPI template up and running.

---

## 📌 Table of Contents

1. [Install Dependencies](#install-dependencies)
2. [Setup Virtual Environment](#setup-virtual-environment)
3. [Project Structure](#project-structure)
4. [Initialize the Database](#initialize-the-database)
5. [Run the Application](#run-the-application)
6. [Testing API Endpoints](#testing-api-endpoints)

---

## 📦 Install Dependencies

Run the following command to install all necessary dependencies:

```bash
pip install fastapi uvicorn sqlmodel "sqlalchemy[asyncio]" asyncpg aiomysql \
            python-multipart pydantic-settings
```

### 📖 Dependencies Breakdown:

- **`fastapi`** → The core FastAPI framework.
- **`uvicorn`** → ASGI server for running FastAPI.
- **`sqlmodel`** → Combines SQLAlchemy and Pydantic for models and schemas.
- **`sqlalchemy[asyncio]`** → Enables async database operations.
- **`asyncpg`** → PostgreSQL async driver.
- **`aiomysql`** → MySQL async driver.
- **`python-multipart`** → Required for form-data support.
- **`pydantic-settings`** → Loads environment variables using Pydantic.

After installation, save dependencies to a `requirements.txt` file:

```bash
pip freeze > requirements.txt
```

---

## 🛠 Setup Virtual Environment

### Step 1: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 2: Activate the Virtual Environment

**For Windows:**

```bash
venv\Scripts\activate
```

**For macOS/Linux:**

```bash
source venv/bin/activate
```

### Step 3: Upgrade `pip`

```bash
pip install --upgrade pip
```

---

## 📂 Project Structure

Run the following command to create the project folder structure:

```bash
mkdir -p backend/app/routes
cd backend && touch app/main.py app/models.py app/database.py \
                  app/routes/todo.py app/config.py app/__init__.py \
                  .env requirements.txt
```

Your folder structure should now look like this:

```bash
backend/
│── app/
│   ├── main.py          # Entry point to start the app
│   ├── models.py        # Database models & schemas
│   ├── database.py      # Database connection setup
│   ├── routes/
│   │   ├── todo.py     # To-Do list API endpoints
│   ├── config.py       # Environment variable management
│   ├── __init__.py     # Marks 'app' as a package
│── .env                # Configuration for database & secrets
│── requirements.txt    # Dependencies
```

---

## 🗄 Initialize the Database

Before starting the application, ensure the database is set up.

### Step 1: Configure Environment Variables (`.env`)

Create a `.env` file with database connection details:

```env
DATABASE_TYPE=sqlite
DB_USERNAME=root
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=test.db
```

### Step 2: Initialize Database Tables

Run the following command to ensure database tables are created at startup:

```bash
uvicorn app.main:app --reload
```

This will trigger FastAPI's startup event, creating tables automatically.

---

## 🚀 Run the Application

To start the FastAPI server, run:

```bash
uvicorn app.main:app --reload
```

- `--reload` enables auto-reloading on code changes (for development use only).
- The API will be accessible at: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**
- Swagger UI (API documentation) will be available at: **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

---

## 📌 Testing API Endpoints

Use `curl` or **Swagger UI** to test the API endpoints.

### **Create a To-Do**

```bash
curl -X POST "http://127.0.0.1:8000/todos" \
     -H "Content-Type: application/json" \
     -d '{"title": "Buy groceries", "description": "Milk, Bread, Cheese", "completed": false}'
```

### **Retrieve All To-Dos**

```bash
curl -X GET "http://127.0.0.1:8000/todos"
```

### **Update a To-Do**

```bash
curl -X PUT "http://127.0.0.1:8000/todos/1" \
     -H "Content-Type: application/json" \
     -d '{"title": "Buy groceries", "description": "Eggs, Milk", "completed": true}'
```

### **Delete a To-Do**

```bash
curl -X DELETE "http://127.0.0.1:8000/todos/1"
```

---

## 🎯 Summary of Commands

### **1️⃣ Create Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate  # (or venv\Scripts\activate on Windows)
pip install --upgrade pip
```

### **2️⃣ Install Dependencies**

```bash
pip install fastapi uvicorn sqlmodel "sqlalchemy[asyncio]" asyncpg aiomysql python-multipart pydantic-settings
pip freeze > requirements.txt
```

### **3️⃣ Setup Project Structure**

```bash
mkdir -p backend/app/routes
cd backend && touch app/main.py app/models.py app/database.py \
                  app/routes/todo.py app/config.py app/__init__.py \
                  .env requirements.txt
```

### **4️⃣ Run FastAPI Server**

```bash
uvicorn app.main:app --reload
```

This document provides all essential commands for setting up and running the FastAPI template. 🚀
