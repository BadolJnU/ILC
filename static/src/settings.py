"""
Django settings for src project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '05q*wkejww#xbmiuagfn95fth8sle7#d20wfa-j4hvesc5)++f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'photologue',
    'sortedm2m',
    'eventManager',
    'noticeboard',
    'home',
    'teachers',
    'study_materials',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'tinymce',
]
SITE_ID = 1
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'src.urls'

from photologue import PHOTOLOGUE_APP_DIR
TEMPLATE_DIRS = (
    PHOTOLOGUE_APP_DIR,
)


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/photologue'),],
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

WSGI_APPLICATION = 'src.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Dhaka'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_ROOT = BASE_DIR+"/media"
MEDIA_URL = '/media/'
STATIC_ROOT = BASE_DIR+"/static"
STATICFILES_DIRS = [
    BASE_DIR,
]

PHOTOLOGUE_GALLERY_SAMPLE_SIZE = 4

#'plugins': "table,spellchecker,paste,searchreplace",

# TinyMCE settings
TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced",
    'skin': "o2k7",
    'skin_variant': "silver",
    'relative_urls': False,
    'width': "900",
    'height': "500",
    'theme_advanced_toolbar_location': "top",
    'theme_advanced_toolbar_align': "left",
    'theme_advanced_statusbar_location': "bottom",
    'theme_advanced_resizing': True,
    'element_format': "html",
    'plugins' : "contextmenu,directionality,fullscreen,paste,preview,searchreplace,spellchecker,visualchars,wordcount,table",
    'theme_advanced_buttons3_add' : "tablecontrols",
    'table_styles' : "Header 1=header1;Header 2=header2;Header 3=header3",
    'table_cell_styles' : "Header 1=header1;Header 2=header2;Header 3=header3;Table Cell=tableCel1",
    'table_row_styles' : "Header 1=header1;Header 2=header2;Header 3=header3;Table Row=tableRow1",
    'table_cell_limit' : 100,
    'table_row_limit' : 5,
    'table_col_limit' : 5,
    'table_inline_editing': True,
}

# TinyMCE settings end