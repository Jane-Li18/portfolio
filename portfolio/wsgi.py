import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

application = WhiteNoise(
    get_wsgi_application(),
    root=str(BASE_DIR / "staticfiles"),
    prefix="/static/",
    max_age=604800
)

# Optional: For local development alias
app = application
