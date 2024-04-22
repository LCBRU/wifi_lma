from .base import *
import pymysql
pymysql.install_as_MySQLdb()


print('*'*50)
print('Using Production environment')
print('*'*50)

DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["SECRET_KEY"]

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = [os.environ["ALLOWED_HOSTS"]]

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

WAGTAILADMIN_BASE_URL = os.environ["WAGTAILADMIN_BASE_URL"]
CSRF_TRUSTED_ORIGINS = [os.environ["WAGTAILADMIN_BASE_URL"]]

STATIC_ROOT = os.environ["STATIC_PATH"]
STATIC_URL = os.environ["STATIC_URL"]

MEDIA_ROOT = os.environ["MEDIA_PATH"]
MEDIA_URL = os.environ["MEDIA_URL"]

DEFAULT_FROM_EMAIL = os.environ["DEFAULT_FROM_EMAIL"]

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.environ["DATABASE_ENGINE"],
        "HOST": os.environ["DATABASE_HOST"],
        "NAME": os.environ["DATABASE_NAME"],
        "USER": os.environ["DATABASE_USER"],
        "PASSWORD": os.environ["DATABASE_PASSWORD"]
    }
}

try:
    from .local import *
except ImportError:
    pass
