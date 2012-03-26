# Django settings for dss project.

import sys
import os
import django
#from dss.questions.views import get_script_name

# calculated paths for django and the site
# used as starting points for various other paths
DJANGO_ROOT = os.path.dirname(os.path.realpath(django.__file__))
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

BASE_SITE = os.path.realpath(os.path.join(SITE_ROOT, os.path.pardir))
HOME_DIR = os.path.realpath(os.path.join(BASE_SITE, os.path.pardir))
# Initialise SCRIPT_NAME
# SCRIPT_NAME is the name of the directory where the wsgi script lies
if 'SCRIPT_NAME' not in os.environ:
    os.environ['SCRIPT_NAME'] = '/'
    URL_PREFIX = os.environ['SCRIPT_NAME']
else:    
    URL_PREFIX = os.environ['SCRIPT_NAME']
if 'DSS_PUBLIC' not in os.environ:
    os.environ['DSS_PUBLIC'] = '/'
    DSS_PUBLIC = os.environ['DSS_PUBLIC']
else:    
    DSS_PUBLIC = os.environ['DSS_PUBLIC']
#FORCE_SCRIPT_NAME = '/'+URL_PREFIX
#if SITE_ROOT not in sys.path:
#    sys.path.append(SITE_ROOT)
GRAPPELLI_ADMIN_TITLE = "DSS"
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
      # For normal set up:
        'NAME': os.path.join(SITE_ROOT, 'database.db'),
      # For the lero server:
      # 'NAME':  '/home/dss/data/dss/dss.db',
#'/var/www/dss/dss.db', # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Dublin'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
#data = os.path.pardir
MEDIA_ROOT = DSS_PUBLIC+"/media/"

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = URL_PREFIX+'/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(DSS_PUBLIC, 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = URL_PREFIX+'/static/'#SITE_ROOT+'/static/'#'/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = URL_PREFIX+'/media/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(DSS_PUBLIC, 'media/static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '+)*ae)+l$=19)3(ot&4!n+mij2j^is*g*sv!4&!!brcs!(jd&d'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.csrf.CsrfResponseMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_SITE, 'templates')#'/var/www/dss/templates'
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'questions',
    'auth',
    'recommendations',
    'django.contrib.markup',
    'grappelli',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    'django.contrib.sessions',
    # Uncomment the next line to enable admin documentation:
    #'django.contrib.admindocs',
)

TEMPLATE_CONTEXT_PROCESSORS = (
      "django.contrib.auth.context_processors.auth",
      "django.core.context_processors.request",
      "django.core.context_processors.debug",
      "django.core.context_processors.i18n",
	  "django.core.context_processors.static",
      "django.core.context_processors.media",
      "django.contrib.messages.context_processors.messages",
)


AUTH_PROFILE_MODULE = 'auth.UserProfile'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
