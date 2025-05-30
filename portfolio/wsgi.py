"""
WSGI config for portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

# Define the WSGI application callable
application = get_wsgi_application()

# If you want to use 'app' locally, you can create a reference
# but keep 'application' as the main callable for Vercel
app = application
