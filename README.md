# Learning Log

Django-приложение: темы и записи пользователей.

## Запуск через Docker Compose

1. Создайте файл `.env` со значениями:
   DJANGO_SECRET_KEY, DJANGO_DEBUG, DJANGO_ALLOWED_HOSTS,
   DJANGO_CSRF_TRUSTED_ORIGINS, DJANGO_USE_HTTPS, SQLITE_PATH,
   APP_BIND_IP, APP_PORT
2. `docker compose up -d --build`
3. `docker compose exec web python manage.py createsuperuser`