release: python manage.py collectstatic --noinput
web: gunicorn UYA_website.wsgi:application --bind 0.0.0.0:$PORT
