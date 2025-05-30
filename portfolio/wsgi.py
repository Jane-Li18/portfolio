"""
WSGI config for portfolio project.
Modified for Vercel deployment with WhiteNoise support.
"""

import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'
BASE_DIR = Path(__file__).resolve().parent.parent

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

# Base Django application
django_application = get_wsgi_application()

# Wrap with WhiteNoise for static files
application = WhiteNoise(
    django_application,
    root=os.path.join(BASE_DIR, 'staticfiles'),
    prefix='/static/',
    max_age=604800  # 1 week cache
)

# Optional: For local development alias
app = application
