# AIRMAN Core Level 1 — Maverick + Skynet Implementation

This project implements a minimal production-focused AIRMAN Core platform that combines authentication, learning management, and scheduling capabilities within a unified system. The goal of this implementation is to demonstrate practical full-stack architecture using modern engineering practices, including role-based access control (RBAC), API-driven development, and containerized deployment.

The application consists of a React frontend, a FastAPI backend, and a PostgreSQL database, all orchestrated through Docker Compose to ensure consistent and reproducible setup across environments.

---

## System Overview

The platform is divided into three main functional areas:

1. Authentication and Role-Based Access Control (RBAC)
2. Learning Module inspired by Maverick-style content management
3. Scheduling Module inspired by Skynet-style booking workflows

Users interact with the system through a web interface, while the backend handles authorization, data validation, and business logic through REST APIs.

---

## Technology Stack

### Backend
The backend is built using FastAPI with SQLAlchemy ORM and PostgreSQL for data storage. JWT authentication is used to secure API endpoints and enforce role-based permissions. Pydantic models are used for input validation and structured request handling.

### Frontend
The frontend is developed using React with TypeScript, React Router for navigation, Axios for API communication, and React Hook Form for form validation.

### DevOps
Docker Compose is used to run the frontend, backend, and database services together. GitHub Actions provides continuous integration by running lint checks, tests, and build processes automatically.

---

## Architecture Overview

The system follows a simple three-layer architecture:

React Frontend → FastAPI Backend → PostgreSQL Database

Users authenticate through the frontend, receive a JWT token, and access protected routes based on their assigned roles. The backend enforces RBAC rules on all protected endpoints.

---

## Roles and Permissions

Admin users are responsible for managing instructors, approving scheduling requests, and overseeing system operations.

Instructor users can create courses, manage lessons, assign quizzes, and define availability for scheduling.

Student users can view learning content, attempt quizzes, and request booking sessions with instructors.

---

## Setup Instructions

### Running with Docker (Recommended)

Clone the repository:
  https://github.com/gowtham1582000/airman-level1-maverick-skynet.git

Start all services:


After the containers start successfully, access:

Backend API documentation:

http://localhost:8000/docs

Frontend application:

http://localhost:5173

---

### Running Locally Without Docker

Backend setup:

cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload


Frontend setup:


---

## Key Technical Decisions and Tradeoffs

FastAPI was selected because of its strong typing support, built-in validation, and minimal boilerplate compared to traditional backend frameworks. SQLAlchemy ORM was used to maintain clear relationships between entities such as courses, lessons, and bookings.

JWT authentication was chosen to keep the backend stateless and scalable. Docker Compose was used to simplify development setup and ensure consistency across environments.

The scheduling module uses straightforward time overlap logic for conflict detection instead of complex calendar frameworks to keep the implementation focused and understandable.

---

## API Documentation

Interactive API documentation is available via Swagger UI:

http://localhost:8000/docs

Main API groups include authentication endpoints, learning module endpoints, and scheduling endpoints.

---

## Sample API Requests

Login request example:

POST /auth/login

{
"email": "student@test.com
",
"password": "123456"
}


Booking creation example:

POST /schedule/book


Booking creation example:

POST /schedule/book
{
"instructor_id": 1,
"start_time": "2026-01-01T10:00:00",
"end_time": "2026-01-01T11:00:00"
}


---

## Testing

Backend tests can be executed using:
cd backend
pytest


Tests include authentication validation, booking conflict detection, and integration scenarios.

---

## Continuous Integration

GitHub Actions automatically runs lint checks, backend tests, and frontend build verification whenever changes are pushed to the repository.

---

## Demo Credentials

Admin user:
admin@test.com / 123456

Instructor user:
instructor@test.com / 123456

Student user:
student@test.com / 123456

---

## Final Notes

This implementation prioritizes clarity, modularity, and maintainability while demonstrating the core architectural concepts required for AIRMAN Core Level 1. The focus is on building a clean and understandable foundation rather than implementing unnecessary complexity.
