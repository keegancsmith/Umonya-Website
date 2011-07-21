# Django settings for umonya project.
# For settings relevant to deployment, search the document for the word DEPLOY

import os.path
project_dir = os.path.abspath(os.path.dirname(__file__))

# DEPLOY set to False
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# DEPLOY set this to the local postgresql or mysql db
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(project_dir, 'umonya.db'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# Locale
TIME_ZONE = 'Africa/Johannesburg'
LANGUAGE_CODE = 'en-za'
USE_I18N = True
USE_L10N = True

# User uploaded files variables. Currently not used
MEDIA_ROOT = ''
MEDIA_URL = ''

# Static file locations. DEPLOY The first two settings should be modified when
# deploying static files to a seperate URL.
STATIC_ROOT = ''
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
STATICFILES_DIRS = ()
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# DEPLOY Change this value for actual deployed sites
SECRET_KEY = 'mn=y5m0vfbcq1m6(84pkoove40&rel_^yzs$te4oq1c8ug^zsr'

# Misc
SITE_ID = 1
ROOT_URLCONF = 'umonya.urls'
ADMINS = (
    ('Umonya Admins', 'admins@umonya.co.za'),
)
MANAGERS = ADMINS

# Template Settings
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
TEMPLATE_DIRS = (
    os.path.join(project_dir, 'templates'),
)


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'umonya.apply',
    'umonya.content',
)


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
