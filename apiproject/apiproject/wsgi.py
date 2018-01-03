"""
WSGI config for apiproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application
from os.path import join,dirname,abspath
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
PROJECT_DIR = dirname(dirname(abspath(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "apiproject.settings")
sys.path.insert(0,PROJECT_DIR)
