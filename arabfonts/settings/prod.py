from pickle import FALSE

from arabfonts.settings.dev import ALLOWED_HOSTS, DEBUG
from .base import *
import os
from django.core.management.utils import get_random_secret_key


SECRET_KEY = 'django-insecure-(w4!+4bfxa5%)esio)egs0*ybll_lah4h1-z(4c5+g$vms00t@'
# SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key())
DEBUG = False
# DEBUG = os.getenv("DEBUG", "False") == "True"
# ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")
ALLOWED_HOSTS = ['arabfonts.herokuapp.com', '127.0.0.1' ]
# DEVELOPMENT_MODE = os.getenv("DEVELOPMENT_MODE", "False") == "True"