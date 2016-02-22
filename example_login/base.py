# -*- encoding: utf-8 -*-
"""
Django settings for login project.
"""
from django.core.urlresolvers import reverse_lazy

DEBUG = True
TESTING = False

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# We use the 'SITE_NAME' for the name of the database and the name of the
# cloud files container.
SITE_NAME = 'app_login'

ADMINS = (
    ('admin', 'code@pkimber.net'),
)

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/London'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-gb'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '#9x3dk(nl82sihl7c^u_#--yp((!g2ehd_1pmp)fpgx=h9(l9='

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'reversion.middleware.RevisionMiddleware',
)

ROOT_URLCONF = 'example_login.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'example_login.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
            'string_if_invalid': '**** INVALID EXPRESSION: %s ****',
        },
    },
]

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'compressor',
    'reversion',
    'base',
    'example_login',
    'login',
    'mail',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
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

# Celery
BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
# https://kfalck.net/2013/02/21/run-multiple-celeries-on-a-single-redis
CELERY_DEFAULT_QUEUE = '{}'.format(SITE_NAME)
# http://celery.readthedocs.org/en/latest/userguide/tasks.html#disable-rate-limits-if-they-re-not-used
CELERY_DISABLE_RATE_LIMITS = True

# django-compressor
COMPRESS_ENABLED = False # defaults to the opposite of DEBUG

# See the list of constants at the top of 'mail.models'
MAIL_TEMPLATE_TYPE = 'django'
DEFAULT_FROM_EMAIL = 'notify@pkimber.net'
# mandrill
#EMAIL_BACKEND = 'djrill.mail.backends.djrill.DjrillBackend'
#MANDRILL_API_KEY = get_env_variable('MANDRILL_API_KEY')
#MANDRILL_USER_NAME = get_env_variable('MANDRILL_USER_NAME')

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

FTP_STATIC_DIR = None
FTP_STATIC_URL = None

# URL where requests are redirected after login when the contrib.auth.login
# view gets no next parameter.
LOGIN_REDIRECT_URL = reverse_lazy('project.dash')

SENDFILE_BACKEND = 'sendfile.backends.development'
SENDFILE_ROOT = 'media-private'
