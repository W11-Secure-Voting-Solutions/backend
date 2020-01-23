import socket
from .base import *  # pylint: disable=W0614

INTERNAL_IPS += ["127.0.0.1"]

# tricks to have debug toolbar when developing with docker
ip = socket.gethostbyname(socket.gethostname())
INTERNAL_IPS += [ip[:-1] + "1"]

STATIC_URL = "/static/"

INSTALLED_APPS += (
    "django_extensions",
    "debug_toolbar",
)

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s")
