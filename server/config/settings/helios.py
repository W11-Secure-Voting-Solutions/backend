import json
from ..helpers.env import env

# add admins of the form:
#    ('Ben Adida', 'ben@adida.net'),
# if you want to be emailed about errors.
ADMINS = ()

MANAGERS = ADMINS

# is this the master Helios web site?
MASTER_HELIOS = False

# show ability to log in? (for example, if the site is mostly used by voters)
# if turned off, the admin will need to know to go to /auth/login manually
SHOW_LOGIN_OPTIONS = True

# sometimes, when the site is not that social, it's not helpful
# to display who created the election
SHOW_USER_INFO = True

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = "UTC"

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "en-us"

SITE_ID = 1


INTERNAL_IPS = []

##
## HELIOS
##


# a relative path where voter upload files are stored
VOTER_UPLOAD_REL_PATH = "voters/%Y/%m/%d"

# Change your email settings
DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL", default="ben@adida.net")
DEFAULT_FROM_NAME = env("DEFAULT_FROM_NAME", default="Ben for Helios")
SERVER_EMAIL = "%s <%s>" % (DEFAULT_FROM_NAME, DEFAULT_FROM_EMAIL)

LOGIN_URL = "/auth/"
LOGOUT_ON_CONFIRMATION = True


# The two hosts are here so the main site can be over plain HTTP
# while the voting URLs are served over SSL.
URL_HOST = env("URL_HOST", default="http://localhost:8000").rstrip("/")

# IMPORTANT: you should not change this setting once you've created
# elections, as your elections' cast_url will then be incorrect.
# SECURE_URL_HOST = "https://localhost:8443"
SECURE_URL_HOST = env("SECURE_URL_HOST", default=URL_HOST).rstrip("/")

# election stuff
SITE_TITLE = env("SITE_TITLE", default="Helios Voting")
MAIN_LOGO_URL = env("MAIN_LOGO_URL", default="/static/logo.png")
ALLOW_ELECTION_INFO_URL = env("ALLOW_ELECTION_INFO_URL", default="0") == "1"

# FOOTER links
FOOTER_LINKS = json.loads(env("FOOTER_LINKS", default="[]"))
FOOTER_LOGO_URL = env("FOOTER_LOGO_URL", default=None)

WELCOME_MESSAGE = env("WELCOME_MESSAGE", default="This is the default message")

HELP_EMAIL_ADDRESS = env("HELP_EMAIL_ADDRESS", default="help@heliosvoting.org")

AUTH_TEMPLATE_BASE = "server_ui/templates/base.html"
HELIOS_TEMPLATE_BASE = "server_ui/templates/base.html"
HELIOS_ADMIN_ONLY = False
HELIOS_VOTERS_UPLOAD = True
HELIOS_VOTERS_EMAIL = True

# are elections private by default?
HELIOS_PRIVATE_DEFAULT = False

LOGIN_REDIRECT_URL = "/"
