"""
Django settings for Qshop project.

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
SECRET_KEY = 'obejpckt73kh)*3c#^d0()n)xn7!q)2p-lx4$@0fzg=%_j7hz#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Buyer',
    'Saller',
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

ROOT_URLCONF = 'Qshop.urls'

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

WSGI_APPLICATION = 'Qshop.wsgi.application'


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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=(
    os.path.join(BASE_DIR,'static'),
)

# 静态文件的收集，如果收集完成之后就要注掉
# STATIC_ROOT=os.path.join(BASE_DIR,'static')

MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'static')

# 公钥
alipay_public_key_string = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA9O64pwEwQQf6wut37u3YjkDsnpTc9SNXRIv1nBP6jWgdd2y5Fr3cY9+qpe2jhSdag1juYsOgjhkQZjTHD5kdrAk2ZoZWPY14YukTLi1HmvduwOOpXCc1ZRgFOnPjHH8PP5t9lDxZar1/9n7R1Z71mjzEyU02FraQg5uKRaCaRLeq01ksoOJOCe5jOlvGBILWnNCuv16EOyCqWbspr2Tg/beBFP1Tzopo/XZg7yNBCl9iMmUwFTqeoY0/7/sxCkO1TMp036tXr6uDFyqi/nWw05uHvkI1RXSV+mYfmrjQ+EPLcsmPY/dj0TcXi1IDAHIKr6yE6r/ZdPhjEZqEcDXZnQIDAQAB
-----END PUBLIC KEY-----"""

# 私钥
alipay_private_key_string = """-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEA9O64pwEwQQf6wut37u3YjkDsnpTc9SNXRIv1nBP6jWgdd2y5Fr3cY9+qpe2jhSdag1juYsOgjhkQZjTHD5kdrAk2ZoZWPY14YukTLi1HmvduwOOpXCc1ZRgFOnPjHH8PP5t9lDxZar1/9n7R1Z71mjzEyU02FraQg5uKRaCaRLeq01ksoOJOCe5jOlvGBILWnNCuv16EOyCqWbspr2Tg/beBFP1Tzopo/XZg7yNBCl9iMmUwFTqeoY0/7/sxCkO1TMp036tXr6uDFyqi/nWw05uHvkI1RXSV+mYfmrjQ+EPLcsmPY/dj0TcXi1IDAHIKr6yE6r/ZdPhjEZqEcDXZnQIDAQABAoIBAQCzYy/saMttpal8HzdMz/heX6CtmLun8sVUl+k/8cX80Tdbo06AIHgM0eDK/BxaRnNdZcHapgquaB8BrD/q5aq8uFaWimcZV8bHMotws4sRLY15SoRc0P6jVw9lO0EoOsrxPDGiYvzeV4IkB8gpW+3nlABQqvMleXqoWT/RNQonrqpnqmOp4as41iL9c/7J7znzxBeBZkDGEwrCx/85muXHjkDI/sjCYfkVx1uyQ9LBaBtpoTxnDUXQRdhI+RmpCilqgQi0Rbt9b3np9KmlfNVldK8sd0LRygki3g1zNnMK+IaNSMgBLlvbIgzuvtw6sNpM/RUjUQx80tHrYDhJu/tBAoGBAPytxYsWXg55UVW6LSgb2SrwZaQ0+qilFv8wnrS338wwTt6tM8scCwDQkvdfR5D7THhvsUBrJ0O5p8l6FFXSrRmo3966YNpNNBoHp20pfscirXo1tlSc7QHdfAWzReIgRvyh+VQAaE0yDbL7H6c1Rv7MKDhW0EN+2WyYMNiejEoRAoGBAPgm4mzyUHcgQzeVclWTuOXvpAA71yOk/mUCv72CWUftJducUZHzLCY9QnfBmbUj8yBze1UJHS4WBDZf9pjmfSjghJPztX2Y2gzzH/e5HxGojlMpI7FKrt7Vw+rYf/YS2CoRDDHBxFe1XYWFC6t+YdIqbEK4M8p5pbrJYbcoe+rNAoGARVVtcjfmATS647odb/cMRSMH0OIUsbfzMnzl35Lg3weWbLW8E4yTXFrfKO/FFHxQRG/phFKiyIumBbvw3ofbpcHYBCbCMsSiek4FXAfZ2MykK3eXm2ogArYCtRG3KFBRCjtrzef6tsv4RFdyHRCadYoRszvnE8433Pt508bVmfECgYEAyAmgcS6MitspFD+WoUGpxUF+tOmILiWtJQQoSL4w9nhHEldasgqSxmiPkjYwkALg1IIDI7NrIGGDF8oX4X272x3SAeptnUeATvwWAv3p+7QitwrsyNhpSxyLCF9qF5VtR8viRqHqgsGjGCT+GUqR1Hd6OfZ/WXLilEYOTTWHXukCgYEAtbaoOez4Y4SRifDkOgVy7J61JSSaQ6lCOLcUgDrUxUY7DCjCc6hPFb7v6rpwcDUIRL1TWC84lqipjgkUbVvfyVedzAEhY3J99VwDyt4pxirGhvI0oZ6bNmYU5wbQ4d+sFlmzb06OiQ8c9pe6y/VJNgvykBySddZ/UnlL6s5l3WM=
-----END RSA PRIVATE KEY-----"""