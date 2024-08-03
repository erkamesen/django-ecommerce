from app.settings.base import *  # noqa

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db-prod.sqlite3',  # noqa
    }
}
