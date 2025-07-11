# 🏦 ORiem Banking System – Backend API

[![Python](https://img.shields.io/badge/python-3.10-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Enterprise-green.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)](LICENSE)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue.svg)](https://www.postgresql.org/)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://github.com/oriem-finance)

> A secure, modular, and scalable backend API for digital banking services — inspired by enterprise architecture practices (e.g., JPMorgan Chase, Revolut, Monzo).

---

## 🔍 Overview

ORiem Banking System is a web-based digital banking backend, built with security, compliance, and performance in mind. It supports:

- Role-based access control (RBAC)
- Secure banking transactions
- Scalable account and user management
- Integration-ready with React / mobile clients
- Logging, auditing, and future-proof modular architecture

---

## 🧱 Architecture

- **Framework:** FastAPI (async REST API)
- **ORM:** SQLAlchemy with PostgreSQL
- **Auth:** JWT + OAuth2 Password Flow
- **Security:** Bcrypt password hashing, input validation, role enforcement
- **Layered Architecture:** API ⟶ Services ⟶ DAO ⟶ Database

---

## 🗂️ Project Structure

```
oriem_backend/
├── app/
│   ├── auth/               # JWT, dependencies, guards
│   ├── config.py           # Env + global settings
│   ├── constants.py        # Enum values, roles
│   ├── database.py         # DB engine and session
│   ├── main.py             # Entrypoint (Uvicorn)
│   ├── middleware/         # CORS, logging
│   ├── models/             # SQLAlchemy models
│   ├── routers/            # API routes (modular)
│   ├── schemas/            # Pydantic DTOs
│   ├── services/           # Business logic layer
│   ├── storage/            # Data access abstraction
│   ├── utils/              # Password, email, validation
│   └── logs/               # Audit & system logs
├── alembic/                # DB migrations
├── tests/                  # Pytest coverage
├── .env                    # Environment variables
├── docker-compose.yml
├── requirements.txt
├── README.md
└── run.sh
```

---

## 📌 Key Features

- 🔐 **User Authentication**: Signup, login, password hashing, access token
- 👥 **RBAC**: Define roles for Customer, Teller, Officer, Admin
- 💳 **Accounts**: Open, close, update customer accounts
- 💰 **Transactions**: Deposit, withdraw, transfer (with atomic operations)
- 📜 **Audit Logging**: System logs for sensitive actions
- 📩 **Email Notifications**: For login alerts, transaction confirmations (optional)
- 📄 **Swagger/OpenAPI**: Auto-generated API docs
- 🧪 **Testing Suite**: Pytest & test clients

---

## ⚙️ Environment Configuration

Create a `.env` file:

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/oriemdb
SECRET_KEY=supersecurekeyhere
ACCESS_TOKEN_EXPIRE_MINUTES=60
ALGORITHM=HS256
```

---

## 🚀 Getting Started

```bash
# Step 1: Clone the repo
git clone https://github.com/oriem-capital/oriem-backend.git
cd oriem-backend

# Step 2: Set up environment
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# Step 3: Initialize DB
alembic upgrade head

# Step 4: Run the app
uvicorn app.main:app --reload
```

---

## 🧪 Run Tests

```bash
pytest tests/
```

---

## 🧾 API Documentation

📍 Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)  
📍 Redoc UI: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🔐 Security Measures

- ✅ JWT Token-based access (Authorization: `Bearer <token>`)
- ✅ Strong password hashing (Bcrypt)
- ✅ Rate limiting (via middleware)
- ✅ Role access control via dependency injection
- ✅ SQL injection prevention via ORM
- ✅ Audit trails (who did what, when)

---

## 🐳 Docker Support

```bash
docker-compose up --build
```

> Optional: Set PostgreSQL or MySQL in `.env` before deploying

---

## 📊 Core API Endpoints

### 👥 Authentication

| Method | Endpoint         | Description         |
|--------|------------------|---------------------|
| POST   | `/auth/signup`   | Register a new user |
| POST   | `/auth/login`    | Login and get token |
| GET    | `/users/me`      | Fetch current user  |

### 💼 Accounts

| Method | Endpoint                  | Description          |
|--------|---------------------------|----------------------|
| POST   | `/accounts/create`        | Open new account     |
| PUT    | `/accounts/{id}/update`   | Modify account       |
| DELETE | `/accounts/{id}/close`    | Close account        |

### 💸 Transactions

| Method | Endpoint                    | Description              |
|--------|-----------------------------|--------------------------|
| POST   | `/transactions/deposit`     | Deposit funds            |
| POST   | `/transactions/withdraw`    | Withdraw funds           |
| POST   | `/transactions/transfer`    | Transfer between accounts|
| GET    | `/transactions/account/{id}`| Get account history      |

---

## 📦 Tech Stack

| Component     | Tool                      |
|---------------|---------------------------|
| Backend       | FastAPI + SQLAlchemy      |
| DB            | PostgreSQL / MySQL        |
| Auth          | JWT + OAuth2              |
| Migration     | Alembic                   |
| Dev Tools     | Uvicorn, Pydantic, Pytest |
| Deployment    | Docker, Docker Compose    |

---

## 🔧 Contribution

```bash
# Format code
black app/
# Run linting
flake8 app/
```

Pull requests welcome! 🙌

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](./LICENSE) file for details.

---

## 🌐 Frontend Project

Want the full frontend (React/Vite) integration?

➡️ [ORIEM CAPITAL FRONTEND](https://github.com/oriem-capital/frontend)  
Built with React, Axios, AuthContext, and Role-based UI.

---

## 🤝 Contact

Built by the **ORiem Engineering Team**  
📫 Contact: team@oriemfinance.com  
🔗 [www.oriemfinance.com](https://www.oriemfinance.com)

---

> Let me know if you want the same version exported to PDF, or need a `README.md` for the React frontend too!
