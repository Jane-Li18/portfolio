from whitenoise import WhiteNoise
from django.core.wsgi import get_wsgi_application
import os
from pathlib import Path

# Set BASE_DIR to your project root (where manage.py lives)
BASE_DIR = Path(__file__).resolve().parent.parent

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings")

# Vercel requires either 'app' or 'handler'
app = get_wsgi_application()
app = WhiteNoise(
    app,
    root=os.path.join(BASE_DIR, "staticfiles"),
    prefix="/static/",
    index_file=True
)

# Required for Vercel
handler = app
