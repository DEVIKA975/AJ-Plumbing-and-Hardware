import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop_backend.settings')

application = get_wsgi_application()
# This file is the entry point for WSGI-compatible web servers to serve the Django application.