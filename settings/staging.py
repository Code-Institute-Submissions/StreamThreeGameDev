from base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Paypal Settings
PAYPAL_NOTIFY_URL = 'http://2cafd30c.ngrok.io/hardtoguessurl/'
PAYPAL_RECIEVER_EMAIL = 'zanirontestb@test.com'

SITE_URL = 'https://streamthreegamedev.herokuapp.com'
ALLOWED_HOSTS.append('streamthreegamedev.herokuapp.com')


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}
