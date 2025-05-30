from whitenoise import WhiteNoise
from django.core.wsgi import get_wsgi_application
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings")

application = get_wsgi_application()
application = WhiteNoise(
    application,
    root=os.path.join(os.path.dirname(__file__), "staticfiles"),
    prefix="/static/",
    index_file=True
)
