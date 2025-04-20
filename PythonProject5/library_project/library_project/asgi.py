import os
from django.core.asgi import get_asgi_application

# Аналогично WSGI, но для асинхронных серверов
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_project.settings')
application = get_asgi_application()
