from ..helpers.env import env

EMAIL_BACKEND = env("EMAIL_BACKEND", default="")
EMAIL_HOST = env("EMAIL_HOST", default="")
EMAIL_USE_TLS = env("EMAIL_USE_TLS", default="")
EMAIL_PORT = env("EMAIL_PORT", default="")
EMAIL_HOST_USER = env("EMAIL_HOST_USER", default="")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD", default="")
