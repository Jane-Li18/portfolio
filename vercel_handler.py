import os
import sys
from pathlib import Path

# Set correct paths
BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Add to Python path
sys.path.append(str(BASE_DIR))

# Configure Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings")

# Initialize Django
from django.core.wsgi import get_wsgi_application
django_app = get_wsgi_application()

# Verify static files directory exists
if not STATIC_ROOT.exists():
    raise RuntimeError(f"Static files directory missing: {STATIC_ROOT}")

# Configure WhiteNoise
from whitenoise import WhiteNoise
app = WhiteNoise(
    django_app,
    root=str(STATIC_ROOT),
    prefix="/static/",
    index_file=True
)

# Vercel-compatible handler
def handler(request, response):
    from io import BytesIO
    from urllib.parse import parse_qs
    
    # Convert Vercel request to WSGI environ
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
    
    # Prepare response
    headers = []
    def start_response(status, response_headers, exc_info=None):
        nonlocal headers
        response.status = int(status.split()[0])
        headers = response_headers
        return lambda data: response.send(data)
    
    # Execute application
    result = app(environ, start_response)
    try:
        for data in result:
            response.send(data)
    finally:
        if hasattr(result, 'close'):
            result.close()
