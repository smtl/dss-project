import os
import sys
import django
# calculated paths for django and the site
# used as starting points for various other paths
DJANGO_ROOT = os.path.dirname(os.path.realpath(django.__file__))
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

os.environ['DJANGO_SETTINGS_MODULE'] = 'dss.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

path = "/home/slowry/"
if path not in sys.path:
    sys.path.append(path)
