"""
WSGI config for wifi_lma project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

load_dotenv()

print('*'*50)
print('Loading Environment')
print('*'*50)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wifi_lma.settings.dev")

application = get_wsgi_application()
