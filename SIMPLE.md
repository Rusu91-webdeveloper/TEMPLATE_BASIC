# 📖 How to Use the FastAPI Template

This guide explains how to effectively integrate and use the provided FastAPI template in your daily development workflow. It covers project setup, database initialization, running the API, and testing endpoints.

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository (If applicable)

If you are using a Git-based workflow, clone the repository first:

```bash
git clone <repository_url>
cd <repository_name>
```

Alternatively, if you downloaded the template as a ZIP file, extract it and navigate into the project folder.

---

## 📦 Setting Up Your Environment

### 2️⃣ Create a Virtual Environment

To isolate dependencies and avoid conflicts, create and activate a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

**For Windows:**
```bash
venv\Scripts\activate
```

**For macOS/Linux:**
```bash
source venv/bin/activate
```

Upgrade `pip`:

```bash
pip install --upgrade pip
```

---

## 📌 Install Dependencies

Use the following command to install all necessary dependencies:

```bash
pip install -r requirements.txt
```

If you need to regenerate the `requirements.txt` file after installing additional packages, run:

```bash
pip freeze > requirements.txt
```

---

## 🏗 Project Structure Overview

Ensure your project follows the expected structure:

```
backend/
│── app/
│   ├── main.py          # Entry point for FastAPI app
│   ├── models.py        # Database models & schemas
│   ├── database.py      # Database connection setup
│   ├── routes/
│   │   ├── todo.py     # API endpoints
│   ├── config.py       # Environment variable management
│   ├── __init__.py     # Marks 'app' as a package
│── .env                # Configuration for database & secrets
│── requirements.txt    # Dependencies
```

---

## 🗄 Database Setup

### 3️⃣ Configure Environment Variables

Create a `.env` file in the project root and define database credentials:

```ini
DATABASE_TYPE=sqlite
DB_USERNAME=root
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=test.db
```

Make sure your database is running before proceeding.

### 4️⃣ Initialize the Database

Run the following command to start the API and ensure tables are created:

```bash
uvicorn app.main:app --reload
```

This will execute FastAPI's startup event, setting up the database automatically.

---

## 🚀 Running the Application

Start the FastAPI server with:

```bash
uvicorn app.main:app --reload
```

- **Swagger UI (API Docs):** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc (Alternative Docs):** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
- **Root API URL:** [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🛠 Testing API Endpoints

You can test API endpoints using **cURL**, **Postman**, or **Swagger UI**.

### **1️⃣ Create a To-Do Item**
```bash
curl -X POST "http://127.0.0.1:8000/todos" \
     -H "Content-Type: application/json" \
     -d '{"title": "Buy groceries", "description": "Milk, Bread, Cheese", "completed": false}'
```

### **2️⃣ Retrieve All To-Dos**
```bash
curl -X GET "http://127.0.0.1:8000/todos"
```

### **3️⃣ Update a To-Do**
```bash
curl -X PUT "http://127.0.0.1:8000/todos/1" \
     -H "Content-Type: application/json" \
     -d '{"title": "Buy groceries", "description": "Eggs, Milk", "completed": true}'
```

### **4️⃣ Delete a To-Do**
```bash
curl -X DELETE "http://127.0.0.1:8000/todos/1"
```

---

## 📝 Adding New Features

If you want to add new routes, create a new Python file inside `app/routes/`.

Example:

1. **Create a new file:** `app/routes/users.py`
2. **Define your FastAPI route:**

```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
def get_users():
    return [{"id": 1, "name": "John Doe"}]
```

3. **Import and include the route in `main.py`**

```python
from fastapi import FastAPI
from app.routes import users

app = FastAPI()
app.include_router(users.router, prefix="/api")
```

Now, your new endpoint will be available at:

```
http://127.0.0.1:8000/api/users
```

---

## ✅ Summary of Essential Commands

### **1️⃣ Setup Virtual Environment & Install Dependencies**
```bash
python -m venv venv
source venv/bin/activate  # (Windows: venv\Scripts\activate)
pip install --upgrade pip
pip install -r requirements.txt
```

### **2️⃣ Run FastAPI Server**
```bash
uvicorn app.main:app --reload
```

### **3️⃣ Testing API Endpoints**
```bash
curl -X GET "http://127.0.0.1:8000/todos"
```

### **4️⃣ Adding a New API Route**
- Create a new file in `app/routes/`
- Define API logic using FastAPI
- Import and include it in `main.py`

---

## 🎯 Best Practices

- **Use virtual environments** to manage dependencies.
- **Commit changes regularly** when using Git.
- **Use `.env` files** to manage environment-specific configurations.
- **Follow proper API versioning** (`/api/v1/...`).
- **Write unit tests** to ensure API stability.

---

## 🎉 Conclusion

This guide provides a structured way to integrate and work with the FastAPI template efficiently. With this setup, you can start developing and extending your FastAPI application immediately. 🚀

