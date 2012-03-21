import os
import sys

# The following code allows the dss.wsgi file to find the dss project
# You may have to change this if you do not use the default file layout
DSS_PUBLIC = os.path.dirname(os.path.realpath(__file__))
PUBLIC_HTML = os.path.realpath(os.path.join(DSS_PUBLIC, os.path.pardir))
os.environ['PUBLIC_HTML'] = PUBLIC_HTML
HOME_DIR = os.path.realpath(os.path.join(PUBLIC_HTML, os.path.pardir))
DATA = os.path.join(HOME_DIR, 'data')

# Line below is inserted by the Makefile because the project name is a variable.
# This allows the wsgi file to find the code base.
# ###################################################################
#CODE_BASE = os.path.join(DATA, 'dss')
# ###################################################################

DATA_DIR='/home/slowry/data/dss'

sys.path.append(DATA_DIR)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
_application = django.core.handlers.wsgi.WSGIHandler()

def application(environ, start_response):
    os.environ['SCRIPT_NAME'] = os.path.dirname(environ['SCRIPT_NAME'])
    os.environ['DSS_PUBLIC'] = DSS_PUBLIC
    return _application(environ, start_response)
