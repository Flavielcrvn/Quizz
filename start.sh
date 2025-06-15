export PORT=${PORT:-8000}  # Définit le port par défaut à 8000 si non défini (Render définit automatiquement PORT)

python manage.py migrate --noinput
python manage.py collectstatic --noinput
gunicorn Quizz.wsgi:application --bind 0.0.0.0:$PORT