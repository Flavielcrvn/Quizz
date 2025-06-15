#!/bin/bash

export PORT=${PORT:-8000}

python manage.py migrate --noinput
python manage.py collectstatic --noinput
gunicorn Quizz.wsgi:application --bind 0.0.0.0:$PORT