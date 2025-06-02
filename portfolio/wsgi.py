import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
from pathlib import Path

# Set correct base directory (where manage.py lives)
BASE_DIR = Path(__file__).resolve().parent.parent

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings")

# Create WSGI application
django_app = get_wsgi_application()

# Wrap with WhiteNoise
application = WhiteNoise(
    django_app,
    root=str(BASE_DIR / "staticfiles"),
    prefix="/static/",
    index_file=True
)

# Vercel-specific requirements
app = application
handler = app  # Required for Vercel Python runtime
