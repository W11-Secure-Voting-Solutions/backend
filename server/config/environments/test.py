from .base import *  # pylint: disable=W0614

DEBUG = False
TEMPLATES[0]["OPTIONS"]["debug"] = False

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}

# Use fast password hasher so tests run faster
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

TEST_RUNNER = "config.runner.PytestTestRunner"

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s")
