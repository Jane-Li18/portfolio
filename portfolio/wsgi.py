import os
from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler

# Set default Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

# Vercel-specific configuration
if os.environ.get('VERCEL'):  # Detect Vercel environment
    # Force Django to handle static files directly
    application = StaticFilesHandler(get_wsgi_application())
else:
    # Local development configuration
    application = get_wsgi_application()
