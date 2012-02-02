import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'dss.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

path = '/var/www/'
if path not in sys.path:
    sys.path.append(path)
