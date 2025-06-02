import os
from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

# Always use StaticFilesHandler in production
application = StaticFilesHandler(get_wsgi_application())
