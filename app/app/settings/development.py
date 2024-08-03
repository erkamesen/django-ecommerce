from app.settings.base import *  # noqa


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db-local.sqlite3',  # noqa
    }
}


INSTALLED_APPS += [  # noqa
    'django_extensions',

]
