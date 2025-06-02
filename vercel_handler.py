import os
import sys
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
from pathlib import Path

# Add your project to Python path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings")

# Create standard WSGI application
django_app = get_wsgi_application()

# Wrap with WhiteNoise
app = WhiteNoise(
    django_app,
    root=str(BASE_DIR / "staticfiles"),
    prefix="/static/",
    index_file=True
)

# Vercel requires this specific handler format
def handler(request, response):
    from io import BytesIO
    from urllib.parse import parse_qs
    from werkzeug.datastructures import Headers
    
    body = BytesIO(request.body)
    environ = {
        'REQUEST_METHOD': request.method,
        'PATH_INFO': request.path,
        'QUERY_STRING': request.query,
        'CONTENT_TYPE': request.headers.get('content-type'),
        'CONTENT_LENGTH': request.headers.get('content-length'),
        'wsgi.input': body,
        'wsgi.url_scheme': 'https',
        'SERVER_NAME': 'vercel',
        'SERVER_PORT': '443',
    }
    
    headers = Headers()
    def start_response(status, response_headers, exc_info=None):
        response.status = int(status.split()[0])
        headers.extend(response_headers)
        return lambda data: response.send(data)
    
    result = app(environ, start_response)
    try:
        for data in result:
            response.send(data)
    finally:
        if hasattr(result, 'close'):
            result.close()
