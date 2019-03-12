"""
WSGI config for bricksticker project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

if os.getenv('ENVTYPE') == 'development':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bricksticker.D_settings")
elif os.getenv('ENVTYPE') == 'production':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bricksticker.P_settings")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bricksticker.T_settings")


application = get_wsgi_application()
