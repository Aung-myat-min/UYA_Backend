Backend for Website of United Youth Association of Burma

# UYA Website Backend

This is the backend API for the UYA Website, built with Django and Django REST Framework.  
It provides the core functionality and API endpoints for the website.

---

## Features

- REST API built with Django REST Framework  
- API documentation using Swagger (drf-yasg)  
- Deployed on Render (https://uya-backend.onrender.com)
- Uses Gunicorn as WSGI HTTP server

---

## Getting Started

### Prerequisites

- Python 3.11+  
- PostgreSQL 
- Git

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/htetarkar2246/UYA_Backend.git
   cd UYA_Backend

2. Create and activate a virtual environment:
  ```bash
  python -m venv venv
  source venv/bin/activate  
  ```
  On Windows:
  ```bash
  venv\Scripts\activate
  ```
3.Install dependencies:
```bash
pip install -r requirements.txt
```

4.Create .env file based on .env.example and fill in environment variables:
```bash
DEBUG=True
DATABASE_URL=your-database-url
SECRET_KEY=your-secret-key
```

5.Run migrations:
```bash
python manage.py migrate
```

6.Start the development server:
```bash
python manage.py runserver
```

API Documentation
Interactive API docs are available via Swagger:

Swagger UI: http://localhost:8000/swagger/ or https://uya-backend.onrender.com/swagger/

ReDoc UI: http://localhost:8000/redoc/ or https://uya-backend.onrender.com/redoc/

These endpoints are also deployed and accessible on the production Render URL.

Admin Dashboard 

http://localhost:8000/admin or https://uya-backend.onrender.com/admin/ 
Login using email and password 

Deployment
This project is deployed on Render.com using the following setup:

Python environment

render.yaml configuration file for service setup

Gunicorn as the production WSGI server

Procfile specifying the startup command

Environment Variables
Make sure to set the following environment variables in .env or your deployment environment:

| Variable                    | Description                       |
| --------------------------- | --------------------------------- |
| `DEBUG`                     | Enable/disable debug mode         |
| `SECRET_KEY`                | Django secret key                 |
| `DATABASE_URL`              | PostgreSQL database URL           |
| `DJANGO_SUPERUSER_USERNAME` | Admin username for auto superuser |
| `DJANGO_SUPERUSER_EMAIL`    | Admin email                       |
| `DJANGO_SUPERUSER_PASSWORD` | Admin password                    |

The superuser will be auto-created at deployment if it doesn't exist.
 
Contact
For questions or feedback, contact: htetarkarlevi@gmail.com

License
© United Youth Association of Burma — All rights reserved.


