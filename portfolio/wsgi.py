import os
from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

# Both variables for maximum compatibility
application = StaticFilesHandler(get_wsgi_application())
app = application  # Alias for Vercel
handler = application  # Another common name
