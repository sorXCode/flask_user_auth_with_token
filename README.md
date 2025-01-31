# Flask User Authentication with JSON Web Token

## Overview
This project is a user authentication system built using Flask and JSON Web Tokens (JWT). It provides secure authentication for web applications, enabling user registration, login, and token-based access to protected routes.

## Features
- **User Registration** – Allows users to create accounts.
- **User Login** – Secure authentication using JWT.
- **Token-Based Authentication** – Provides protected endpoints.
- **Password Hashing** – Uses industry-standard security practices.
- **Role-Based Access Control (Optional)** – Restrict access based on user roles.

## Tech Stack
- **Flask** – Lightweight Python web framework.
- **Flask-JWT-Extended** – Secure JWT-based authentication.
- **Flask-SQLAlchemy** – ORM for database management.
- **Flask-Migrate** – Database migrations with Alembic.
- **SQLite/PostgreSQL** – Database options.

## Installation

Clone the repository:
```sh
git clone https://github.com/sorXCode/flask_user_auth_with_token.git
cd flask_user_auth_with_token
```

Create a virtual environment:
```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install dependencies:
```sh
pip install -r requirements.txt
```

## Configuration
Update the `.env` file with your database URL and secret key:
```
SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///site.db  # Change for PostgreSQL if needed
```

## Running the Application

Initialize the database:
```sh
flask db upgrade
```

Run the Flask application:
```sh
flask run
```

## API Endpoints

### User Registration
```
POST /register
```
**Request:**
```json
{
  "username": "example_user",
  "password": "securepassword"
}
```

### User Login
```
POST /login
```
**Request:**
```json
{
  "username": "example_user",
  "password": "securepassword"
}
```
**Response:**
```json
{
  "access_token": "your_jwt_token"
}
```

### Protected Route
```
GET /protected
```
Requires an Authorization header:
```
Authorization: Bearer your_jwt_token
```

## License
This project is licensed under the MIT License.

---

🚀 **Secure your Flask app with JWT authentication today!**
