import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop_backend.settings')

application = get_asgi_application()
# This file is the entry point for ASGI-compatible web servers to serve the Django application.