import os
import sys

DSS_PUBLIC = os.path.dirname(os.path.realpath(__file__))

# DATA_DIR is where the Django code exists
# DATA_DIR is set in the Makefile
DATA_DIR='/home/slowry/data/decisionsupportsystem'
sys.path.append(DATA_DIR)

# This is the settings file for the project
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
_application = django.core.handlers.wsgi.WSGIHandler()

def application(environ, start_response):
    os.environ['SCRIPT_NAME'] = os.path.dirname(environ['SCRIPT_NAME'])
    os.environ['DSS_PUBLIC'] = DSS_PUBLIC
    return _application(environ, start_response)
