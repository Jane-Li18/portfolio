import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise  # Keep using WhiteNoise
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

# Create the WhiteNoise application
application = WhiteNoise(
    get_wsgi_application(),
    root=str(BASE_DIR / "staticfiles"),
    prefix="/static/",
    max_age=604800
)

# Vercel-specific requirements
app = application
handler = application.__call__  # This satisfies Vercel's handler check
