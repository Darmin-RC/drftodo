import os
import django
from django.core.wsgi import get_wsgi_application
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo.settings')

# Inicializa Django
django.setup()

# Crea un superusuario si no existe
User = get_user_model()
if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "darminrc@gmail.com", "D@rmin06")
    print("Superusuario creado exitosamente.")

application = get_wsgi_application()
