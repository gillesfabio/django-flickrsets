#!/usr/bin/env python
import os
import sys

from django.core.management import execute_manager
from django.core.management import setup_environ


ROOT = os.path.dirname(os.path.abspath(__file__))

sys.path.append(os.path.join(ROOT, 'apps'))
sys.path.append(os.path.join(ROOT, '..'))

try:
    import flickrsets_example.settings_local as settings
except ImportError:
    sys.stderr.write(
        "Error: tried importing 'settings_local.py' and 'settings.py' "
        "but neither could be found (or they are throwing an ImportError). "
        "Please, come back and try again later.")
    raise

setup_environ(settings)

if __name__ == "__main__":
    execute_manager(settings)
