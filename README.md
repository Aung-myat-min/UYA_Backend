Backend for Website of United Youth Association of Burma

# UYA Website Backend

This is the backend API for the UYA Website, built with Django and Django REST Framework.  
It provides the core functionality and API endpoints for the website.

---

## Features

- RESTful API using Django REST Framework
- API documentation with Swagger (drf-yasg)
- Image storage via [Cloudinary Free Plan](https://cloudinary.com/)
- Custom user model with email-based login
- Admin dashboard with inline project image management
- Superuser-only audit log viewer (action logs, deletions, updates)
- Deployed on [Render](https://uya-backend.onrender.com)
- PostgreSQL database
- Gunicorn as WSGI HTTP server

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
```
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
   DJANGO_SUPERUSER_USERNAME=<SUPERUSER_USERNAME>
   DJANGO_SUPERUSER_EMAIL=<SUPERUSER_EMAIL>
   DJANGO_SUPERUSER_PASSWORD=<SUPERUSER_PASSWORD>
   CLOUDINARY_URL=cloudinary://<API_KEY>:<API_SECRET>@<CLOUD_NAME>
   EMAIL_HOST_USER=<HOST_EMAIL>
   EMAIL_HOST_PASSWORD=<HOST_PASSWORD>
   DEFAULT_FROM_EMAIL=<DEFAULT_EMAIL>
   ORG_EMAIL=<ORG_EMAIL>
   ```

5.Run migrations:
   ```bash
   python manage.py migrate
   ```

6.Start the development server:
   ```bash
   python manage.py runserver
   ```

### API Documentation
## Interactive API docs are available via Swagger:

Swagger UI:
 ```bash
http://localhost:8000/swagger/ or https://uya-backend.onrender.com/swagger/
```

ReDoc UI:
 ```bash
http://localhost:8000/redoc/ or https://uya-backend.onrender.com/redoc/
```

These endpoints are also deployed and accessible on the production Render URL.

### Contact Form Email
Users can send messages using the Contact Us form from the frontend.

## This endpoint:

Sends the message to your organizational email

Automatically sends an acknowledgment reply to the sender
 ```bash
POST /api/contact/
```

Request Example: 

 ```bash
{
  "name": "John Doe",
  "email": "john@example.com",
  "subject": "Volunteering Opportunities",
  "message": "I'd love to get involved!"
}

Response:
{
  "status": "success",
  "message": "Message received successfully",
  "data": {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "subject": "Volunteering Opportunities",
    "message": "I'd love to get involved!"
  }
}
```

### Admin Dashboard 
 ```bash
http://localhost:8000/admin or https://uya-backend.onrender.com/admin/
```
Login using email and password 

### Superuser-Only Features
-Full audit log via Django LogEntry
-View change details, deletions, and edits
-User Management (Create/Read/Delete)
-User status controls (active/inactive, staff toggle)

### Image Upload (Cloudinary)
Images uploaded via admin or API are stored on Cloudinary.

Environment variable required:
CLOUDINARY_URL=cloudinary://<API_KEY>:<API_SECRET>@<CLOUD_NAME>

### Deployment
This project is deployed on Render.com using the following setup:

-Python environment
-render.yaml configuration file for service setup
-Gunicorn as the production WSGI server
-Procfile specifying the startup command

## Environment Variables
Make sure to set the following environment variables in .env or your deployment environment:

| Variable                    | Description                       |
| --------------------------- | --------------------------------- |
| `DEBUG`                     | Enable/disable debug mode         |
| `SECRET_KEY`                | Django secret key                 |
| `DATABASE_URL`              | PostgreSQL connection string      |
| `CLOUDINARY_URL`            | Cloudinary credentials            |
| `DEFAULT_FROM_EMAIL`        | From email for outgoing mail      |
| `ORG_EMAIL`                 | Email to receive contact messages |
| `DJANGO_SUPERUSER_USERNAME` | Superuser username (auto create)  |
| `DJANGO_SUPERUSER_EMAIL`    | Superuser email                   |
| `DJANGO_SUPERUSER_PASSWORD` | Superuser password                |

The superuser will be auto-created at deployment if it doesn't exist.
 
### Contact
For questions or feedback, contact: htetarkarlevi@gmail.com

### License
© United Youth Association of Burma — All rights reserved.


