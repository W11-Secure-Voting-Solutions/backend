from ..helpers.env import env

# authentication systems enabled
# AUTH_ENABLED_AUTH_SYSTEMS = ['password','facebook','twitter', 'google', 'yahoo']
AUTH_ENABLED_AUTH_SYSTEMS = env("AUTH_ENABLED_AUTH_SYSTEMS", default="google").split(
    ","
)
AUTH_DEFAULT_AUTH_SYSTEM = env("AUTH_DEFAULT_AUTH_SYSTEM", default=None)

GOOGLE_CLIENT_ID = env("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = env("GOOGLE_CLIENT_SECRET")

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backend.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackends",
]

SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "APP": {
            "client_id": GOOGLE_CLIENT_ID,
            "secret": GOOGLE_CLIENT_SECRET,
            "key": "",
        }
    },
    "github": {"SCOPE": ["user", ]},
}
