"""
Django settings for pwc project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
import os

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-wxcgi$6x^f8i4y3qb-vt+un6b0bk*v_@&$(i2p203c807j9rl7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['*']

SITE_ID=1
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'django_recaptcha', 
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.mfa',
     "allauth.usersessions",
     'django.contrib.humanize',
     "captcha",
]
AUTHENTICATION_BACKENDS = ("allauth.account.auth_backends.AuthenticationBackend",)
RECAPTCHA_PUBLIC_KEY = '6LciX1YqAAAAAEabHig-jxTlRgbEweRaqKim0acy'
RECAPTCHA_PRIVATE_KEY = '6LciX1YqAAAAAIyBa5iwPgcN3V_B9IQ1L19-khCw'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    
]
RECAPTCHA_USE_SSL = True 
ACCOUNT_SIGNUP_FORM_CLASS = 'app.forms.AllAuthSignupForm'
ACCOUNT_FORMS={'login':'app.forms.AllAuthLoginForm'}

ROOT_URLCONF = 'pwc.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"templates")],
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
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

WSGI_APPLICATION = 'pwc.wsgi.application'
AUTHENTICATION_BACKENDS = ("allauth.account.auth_backends.AuthenticationBackend",)
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
ACCOUNT_LOGIN_BY_CODE_ENABLED = True
ACCOUNT_EMAIL_VERIFICATION_BY_CODE_ENABLED = True

MFA_SUPPORTED_TYPES = [
    # "webauthn",
    "totp",
    "recovery_codes",
]
MFA_PASSKEY_LOGIN_ENABLED = True
MFA_PASSKEY_SIGNUP_ENABLED = True

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS=[os.path.join(BASE_DIR,"static")]
STATIC_ROOT=os.path.join(BASE_DIR,"assets")
MEDIA_URL='media/'
MEDIA_ROOT=os.path.join(BASE_DIR,"media")
AUTHENTICATION_BACKENDS = (
    # ...
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
    # ...
)
# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
ACCOUNT_EMAIL_REQUIRED=True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'


LOGIN_REDIRECT_URL="/"
LOGOUT_REDIRECT_URL="/"

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587  # or the appropriate port for your SMTP server
EMAIL_USE_TLS = True  # or False if not using TLS
EMAIL_HOST_USER = 'amsproject00@gmail.com'
EMAIL_HOST_PASSWORD = 'aposdpoeglzztyjm'