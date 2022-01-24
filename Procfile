release: python manage.py migrate --noimput
web: gunicorn GestionComercialWeb.wsgi:application --log-file -