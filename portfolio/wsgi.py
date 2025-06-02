import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
from pathlib import Path

# Set up Django settings
BASE_DIR = Path(__file__).resolve().parent.parent
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

# Create the WSGI application
django_app = get_wsgi_application()

# Wrap with WhiteNoise for static files
application = WhiteNoise(
    django_app,
    root=str(BASE_DIR / "staticfiles"),
    prefix="/static/",
    max_age=604800
)

# Vercel requires either 'app' or 'handler'
app = application

# Create a proper handler class for Vercel
class VercelHandler:
    def __init__(self, wsgi_app):
        self.wsgi_app = wsgi_app
    
    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)

# Ensure the handler is a callable object
handler = VercelHandler(application)
