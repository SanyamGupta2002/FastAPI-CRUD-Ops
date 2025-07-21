# FastAPI-CRUD-Ops
CRUD Operations Using FASTAPI

This is a simple REST API built with **FastAPI** that demonstrates basic **CRUD (Create, Read, Update, Delete)** operations. It can be easily extended for real-world applications.

---

## 🧰 Tech Stack

- **FastAPI**
- **Pydantic**
- **Uvicorn** (ASGI Server)
- **SQLite** / PostgreSQL / Any supported DB (via SQLAlchemy or raw SQL)
- **Python 3.8+**

---

## 📁 Project Structure
crud_fastapi/
├── main.py # Main FastAPI app
├── models.py # Pydantic models
├── database.py # DB connection and ORM (if using SQLAlchemy)
├── crud.py # CRUD functions
├── requirements.txt
└── README.md
