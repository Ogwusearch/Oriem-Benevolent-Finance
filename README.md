# 💳 Oriem Benevolent Finance

![CI](https://github.com/your-org/internet-banking-api/actions/workflows/ci.yml/badge.svg)  
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)  
![Docs](https://img.shields.io/badge/docs-OpenAPI-blue)  
![Coverage](https://img.shields.io/badge/coverage-90%25-brightgreen)  
![Code Quality](https://img.shields.io/badge/code%20quality-A-brightgreen)

A modern, secure, microservice-based **online banking system** built with **FastAPI**, designed for modularity, scalability, and developer-friendliness.

---

## 📚 Table of Contents

- [🚀 Features](#-features)  
- [🧱 Architecture](#-architecture)  
- [🛠️ Tech Stack](#️-tech-stack)  
- [📁 Project Structure](#-project-structure)  
- [⚡ Quick Start](#-quick-start)  
- [🔧 Environment Variables](#-environment-variables)  
- [🔐 Authentication](#-authentication)  
- [📘 API Documentation](#-api-documentation)  
- [🧪 Testing](#-testing)  
- [🤝 Contributing](#-contributing)  
- [📅 Changelog](#-changelog)  
- [📃 License](#-license)  
- [📸 Screenshots & Diagrams](#-screenshots--diagrams)  
- [🔒 Security Notes](#-security-notes)

---

## 🚀 Features

- 🔐 **Authentication:** JWT tokens, OAuth2 ready  
- 👤 **User Management:** Registration, login, KYC, profiles  
- 🏦 **Account Lifecycle:** Open, close, balance inquiries  
- 💸 **Transactions:** Internal/external transfers with audit logs  
- 💳 **Card Services:** Card issuance, blocking, controls  
- 🏛️ **Loans:** Application, approval, repayment tracking  
- 🔔 **Notifications:** Email, SMS, push alerts  
- 🧾 **Audit Logging:** Full compliance tracking  
- ⚙️ **Admin Dashboard:** Role-based access control APIs  
- 📘 **OpenAPI Spec:** Modular, auto-generated docs

---

## 🧱 Architecture

```text
Client Apps (Web/Mobile)
        ↓
   [API Gateway]
        ↓
 ┌────────┬────────┬────────┬────────┐
 │ Auth   │ Users  │ Accounts │ Cards │
 └────────┴────────┴────────┴────────┘
       ↓          ↓           ↓
   Payments   Transactions   Loans
       ↓          ↓           ↓
 Notifications   Audit     Admin
````

**Microservices communicate via REST and optionally Kafka events.**

---

## 🛠️ Tech Stack

| Layer          | Technology                      |
| -------------- | ------------------------------- |
| API Gateway    | FastAPI + Traefik / Kong        |
| Microservices  | FastAPI (Python)                |
| Authentication | JWT, OAuth2                     |
| Databases      | PostgreSQL, Redis               |
| Messaging      | Kafka (optional)                |
| Documentation  | OpenAPI 3.0 (Redoc, Swagger UI) |
| CI/CD          | GitHub Actions                  |

---

## 📁 Project Structure

```text
internet-banking-api/
├── gateway/             # API gateway (routing, auth, rate limiting)
├── services/            # Domain microservices
│   ├── auth/
│   ├── users/
│   ├── accounts/
│   ├── transactions/
│   ├── payments/
│   ├── cards/
│   ├── loans/
│   ├── notifications/
│   ├── audit/
│   └── admin/
├── openapi/             # Modular OpenAPI spec files
│   ├── openapi.yaml
│   ├── paths/
│   └── components/
├── k8s/                 # Kubernetes manifests
├── docs/                # Docs, images, Postman collections
└── .github/             # GitHub Actions workflows
```

---

## ⚡ Quick Start

```bash
# Clone the repo
git clone https://github.com/your-org/internet-banking-api.git
cd internet-banking-api

# Copy example env file and edit
cp .env.example .env
# (edit .env to set DB credentials, secrets, etc.)

# Run API Gateway (development mode)
uvicorn gateway.main:app --reload --port 8000
```

Visit API docs at:

* Swagger UI: `http://localhost:8000/docs`
* Redoc: `http://localhost:8000/redoc`

### Example: Login and Get Token

```bash
curl -X POST "http://localhost:8000/auth/login" \
-H "Content-Type: application/json" \
-d '{"email":"user@example.com","password":"securepassword"}'
```

---

## 🔧 Environment Variables

| Variable                      | Description                            | Example                               |
| ----------------------------- | -------------------------------------- | ------------------------------------- |
| `DATABASE_URL`                | PostgreSQL connection string           | `postgresql://user:pass@localhost/db` |
| `REDIS_URL`                   | Redis URL for caching & sessions       | `redis://localhost:6379`              |
| `JWT_SECRET_KEY`              | Secret key to sign JWT tokens          | `supersecretkey`                      |
| `JWT_ALGORITHM`               | Algorithm for JWT signing (e.g. HS256) | `HS256`                               |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Token expiry time in minutes           | `30`                                  |
| `EMAIL_SMTP_SERVER`           | SMTP server for notification emails    | `smtp.mailtrap.io`                    |
| `EMAIL_FROM`                  | Default email sender address           | `noreply@bank.com`                    |
| ...                           | Other service-specific configs         |                                       |

> Keep `.env` out of public repos for security.

---

## 🔐 Authentication

* Uses **JWT Bearer tokens** for protected endpoints.
* Obtain token via `/auth/login`.
* Include token in headers:

```http
Authorization: Bearer <access_token>
```

* OAuth2 flows support planned/optional.

---

## 📘 API Documentation

Modular OpenAPI spec layout:

```text
/openapi/
├── openapi.yaml          # Root spec file
├── paths/
│   ├── auth.yaml
│   ├── users.yaml
│   ├── accounts.yaml
│   └── ...
└── components/
    ├── schemas.yaml
    ├── security.yaml
    └── responses.yaml
```

Preview docs locally with:

```bash
npm install -g redoc-cli
redoc-cli serve openapi/openapi.yaml
```

---

## 🧪 Testing

* Use Postman collection in `/docs/postman_collection.json`.
* Run Pytest inside each service folder:

```bash
pytest tests/
```

* CI pipelines automate tests on PRs.

---

## 🤝 Contributing

See [`CONTRIBUTING.md`](./CONTRIBUTING.md) for guidelines.

Summary:

1. Fork the repo
2. Create feature branch (`git checkout -b feature/your-feature`)
3. Write conventional commit messages
4. Run tests locally
5. Submit Pull Request

---

## 📅 Changelog

See [`CHANGELOG.md`](./CHANGELOG.md) for version history.

---

## 📃 License

MIT © \[Your Company / Name]

---

## 📸 Screenshots & Diagrams

### Architecture Diagram

```ascii
+------------+       +-------------+       +---------------+
| Web/Mobile | <---> | API Gateway | <---> | Microservices |
+------------+       +-------------+       +---------------+
                                      /      |       \       
                             +-------+       |        +-------+
                             |               |                |
                        +--------+      +---------+      +--------+
                        | Auth   |      | Accounts|      | Loans  |
                        +--------+      +---------+      +--------+
```

### Sample API Response

```json
{
  "account_id": "12345",
  "owner": "user@example.com",
  "balance": 10234.56,
  "currency": "USD",
  "status": "active"
}
```

---

## 🔒 Security Notes

* Passwords hashed securely with bcrypt or Argon2.
* JWT tokens signed with strong secret keys.
* HTTPS enforced in production.
* Rate limiting and IP blacklisting via API Gateway (planned).
* Audit logs capture user/admin actions for compliance.
* OAuth2 integration supported/planned.

---

If you want sample code files or help with a microservice next, just ask!

```
```
