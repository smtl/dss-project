import os
import sys
# dss_home is the path to where the dss files are
# dss_base is the path to where the dss folder is located. This is needed for
# the apache server
dss_home = os.path.dirname(os.path.join(os.path.pardir, os.path.dirname(__file__)))
dss_base = os.path.dirname(os.path.join(os.path.pardir, dss_home))

sys.path.insert(0, dss_home)
sys.path.insert(0, dss_base)

os.environ['DJANGO_SETTINGS_MODULE'] = 'dss.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
