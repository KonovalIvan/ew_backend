from django.conf import settings


def pytest_configure():
    settings.DEBUG = False
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'test_db',
        'USER': 'test_user',
        'PASSWORD': 'test_password',
        'HOST': 'localhost',
        'PORT': '5433',
    }
    settings.MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]


def django_db_setup():
    from django.conf import settings
    from django.core.management import call_command
    from django.db import connections

    settings.DEBUG = False

    for alias in connections:
        connection = connections[alias]
        if connection.settings_dict['NAME'] == 'test_db':
            connection.creation.create_test_db(autoclobber=True)

    call_command('migrate')

    yield

    for alias in connections:
        connection = connections[alias]
        if connection.settings_dict['NAME'] == 'test_db':
            connection.creation.destroy_test_db()
