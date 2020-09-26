from ublog.settings import *

ALLOWED_HOSTS = ['*']

DEBUG = True

SECRET_KEY = 'foo'

AUTH_PASSWORD_VALIDATORS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
