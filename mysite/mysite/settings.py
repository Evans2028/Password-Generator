"""import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY: read sensitive settings from the environment

# DEBUG: read from environment; default to False
DEBUG = os.environ.get('DJANGO_DEBUG', 'False').lower() in ('1', 'true', 'yes')

# SECRET_KEY: require it in production (when DEBUG is False)
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
if not SECRET_KEY and not DEBUG:
    raise RuntimeError("DJANGO_SECRET_KEY environment variable is required in production")

# ALLOWED_HOSTS: in production read from DJANGO_ALLOWED_HOSTS as comma-separated list
if DEBUG:
    ALLOWED_HOSTS = []
else:
    raw_hosts = os.environ.get('DJANGO_ALLOWED_HOSTS', '')
    # clean up whitespace and remove empty entries
    ALLOWED_HOSTS = [h.strip() for h in raw_hosts.split(',') if h.strip()]

# Application definition (unchanged)
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'password_generator',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'
# Database and the rest of settings remain unchanged below this line..."""