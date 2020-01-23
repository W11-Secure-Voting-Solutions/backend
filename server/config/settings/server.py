import environ
from ..helpers.env import env

SECRET_KEY = env("DJANGO_SECRET_KEY")

DEBUG = env("DEBUG", default="0") == "1"

# now that setting are deep inside the file structure, we need to manually dig ourselves out
APPS_DIR = environ.Path(__file__) - 3

CORS_ORIGIN_ALLOW_ALL = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_PRELOAD = True
SESSION_COOKIE_HTTPONLY = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
ROOT_URLCONF = "urls"
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")


# *********************** MEDIA ***********************
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ""
MEDIA_ROOT = str(APPS_DIR.path("media"))

# *********************** STATIC ***********************

STATIC_URL = "./static/"
STATICFILES_DIRS = [str(APPS_DIR("static"))]
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

MIDDLEWARE = [
    # secure a bunch of things
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
]

INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.messages",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.staticfiles",
    "rest_framework",
    "corsheaders",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.github",
    "helios_auth.apps.HeliosAuthConfig",
    "helios.apps.HeliosConfig",
    "server_ui.apps.ServerUiConfig",
    "apolloassistant",
)

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [str(APPS_DIR.path("templates")), str(APPS_DIR), ],
        "OPTIONS": {
            "debug": DEBUG,
            "loaders": [
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
            "context_processors": ["django.template.context_processors.request", ],
        },
    },
]
