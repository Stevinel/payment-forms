python manage.py migrate --no-input
exec gunicorn payment_forms.wsgi:application -b 0.0.0.0:8000 --reload