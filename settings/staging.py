from base import *
import dj_database_url


DEBUG = False

DATABASES = {
    'default': dj_database_url.config('CLEARDB_DATABASE_URL')
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
