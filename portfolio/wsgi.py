"""
WSGI config for portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.
Modified for Vercel deployment with WhiteNoise support.
"""

import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise  # Import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

# Base Django application
django_application = get_wsgi_application()

# Wrap with WhiteNoise for static files
application = WhiteNoise(
    django_application,
    root=os.path.join(os.path.dirname(__file__), '../staticfiles'),  # Path to collected static
    prefix='/static/',  # URL prefix
    max_age=604800  # 1 week cache (optional but recommended)
)

# Optional: For local development alias
app = application
