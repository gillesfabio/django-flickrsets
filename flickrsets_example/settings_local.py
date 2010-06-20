# pylint: disable=W0401
from flickrsets_example.settings import *

# Databases
# -----------------------------------------------------------------------------
DB_DIR = os.path.join(PROJECT_ROOT, 'db')
if not os.path.exists(DB_DIR):
    os.makedirs(DB_DIR)

DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'
DATABASES['default']['NAME'] = os.path.join(
    PROJECT_ROOT, 
    'db', 
    'development.sqlite')

# django-debug-toolbar
# -----------------------------------------------------------------------------
#INSTALLED_APPS += ('debug_toolbar',)
#MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
#INTERNAL_IPS = ('127.0.0.1',)
#DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False}

# Caching
# -----------------------------------------------------------------------------
#CACHE_BACKEND = 'dummy://'  # 'file:///var/tmp/django_cache'
#CACHE_MIDDLEWARE_KEY_PREFIX += 'dev_'

# Email
# -----------------------------------------------------------------------------
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025

# Logging
# -----------------------------------------------------------------------------
import logging

log_formatter = logging.Formatter(
    '%(asctime)s [%(levelname)s] -- Django Flickrsets -- %(message)s')
log_handler = logging.StreamHandler()
log_handler.setFormatter(log_formatter)

parsers_log = logging.getLogger('flickrsets.parsers')
parsers_log.addHandler(log_handler)
parsers_log.setLevel(logging.INFO)

managers_log = logging.getLogger('flickrsets.managers')
managers_log.addHandler(log_handler)
managers_log.setLevel(logging.INFO)
