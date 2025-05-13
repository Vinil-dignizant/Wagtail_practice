from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure--@%=ihd)!-w@$7c+26jociqjo=ct@x+8at(300b-6)pa)u3bqf"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Application definition
# Add 'debug_toolbar' to the list of installed apps
INSTALLED_APPS = INSTALLED_APPS + [
    "debug_toolbar",
]


MIDDLEWARE = MIDDLEWARE+[
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]


INTERNAL_IPS = ("127.0.0.1", "127.17.0.1")

try:
    from .local import *
except ImportError:
    pass
