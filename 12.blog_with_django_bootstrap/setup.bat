python manage.py makemigrations
python manage.py migrate
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(email='admin@example.com', is_superuser=True).delete(); User.objects.create_superuser('admin', 'admin@example.com', 'nicai');"
python manage.py runserver
