"""
Django settings for build_project project.

Generated by 'django-admin startproject' using Django 1.11.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(BASE_DIR, 'static')
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v8n-)m72s^)hw^7poyl51&9)=cz28a1vmx@8bcvmqsej2^#q6='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'initial',
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

ROOT_URLCONF = 'build_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR, ],
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

WSGI_APPLICATION = 'build_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles/')
STATICFILES_DIRS = [STATIC_DIR, ]


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'stream_to_console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django_auth_ldap': {
            'handlers': ['stream_to_console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

import ldap
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType


# # Baseline configuration.
AUTH_LDAP_SERVER_URI = "ldap://ldap.nvidia.com"

# AUTH_LDAP_BIND_DN = "cn=svcmobile_promotions,dc=nvidia,dc=com"
# AUTH_LDAP_BIND_PASSWORD = ""
# #AUTH_LDAP_USER_DN_TEMPLATE = "%(user)s@nvidia.com"

AUTH_LDAP_BIND_AS_AUTHENTICATING_USER = True
AUTH_LDAP_USER_DN_TEMPLATE = "%(user)s@nvidia.com"
AUTH_LDAP_USER_SEARCH = LDAPSearch("OU=Users,DC=nvidia,DC=com",
    ldap.SCOPE_SUBTREE, "(objectClass=groupOfNames)")
# # or perhaps:
# # AUTH_LDAP_USER_DN_TEMPLATE = "uid=%(user)s,ou=users,dc=nvidia,dc=com"


# #options
AUTH_LDAP_CONNECTION_OPTIONS = { 
    ldap.OPT_REFERRALS: 0
}

# AUTH_LDAP_USER_SEARCH = LDAPSearch("DC=nvidia,DC=com",
#     ldap.SCOPE_SUBTREE, "(cn=*)")

# Set up the basic group parameters.
# AUTH_LDAP_GROUP_SEARCH = LDAPSearch("ou=groups,dc=nvidia,dc=com",
#     ldap.SCOPE_SUBTREE, "(objectClass=groupOfNames)"
# )
#AUTH_LDAP_GROUP_TYPE = GroupOfNamesType()

# # Simple group restrictions
# AUTH_LDAP_REQUIRE_GROUP = "cn=access-sw-mobile-gerrit-promotions-submitters,ou=GroupID,ou=groups,dc=nvidia,dc=com"
# AUTH_LDAP_DENY_GROUP = "cn=access-sw-mobile-gerrit-promotions-submitters,ou=GroupID,ou=groups,dc=nvidia,dc=com"

# Populate the Django user from the LDAP directory.
AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "member",
    "last_name": "sn",
    "email": "mail"
}

# AUTH_LDAP_PROFILE_ATTR_MAP = {
#     "employee_number": "employeeNumber"
# }

# AUTH_LDAP_USER_FLAGS_BY_GROUP = {
#     "is_active": "cn=access-sw-mobile-gerrit-promotions-submitters,ou=GroupID,ou=groups,dc=nvidia,dc=com",#"cn=active,ou=django,ou=groups,dc=nvidia,dc=com",
#     "is_staff": "cn=access-sw-mobile-gerrit-promotions-submitters,ou=GroupID,ou=groups,dc=nvidia,dc=com",#"cn=staff,ou=django,ou=groups,dc=nvidia,dc=com",
#     "is_superuser": "cn=superuser,ou=access-sw-mobile-gerrit-promotions-submitters,ou=groups,dc=nvidia,dc=com"
# }

# # AUTH_LDAP_PROFILE_FLAGS_BY_GROUP = {
# #     "is_awesome": "cn=access-sw-mobile-gerrit-promotions-submitters,ou=GroupID,ou=groups,dc=nvidia,dc=com",#"cn=awesome,ou=django,ou=groups,dc=nvidia,dc=com",
# # }

# # # Use LDAP group membership to calculate group permissions.
# # AUTH_LDAP_FIND_GROUP_PERMS = True

# # # Cache group memberships for an hour to minimize LDAP traffic
# # AUTH_LDAP_CACHE_GROUPS = True
# # AUTH_LDAP_GROUP_CACHE_TIMEOUT = 3600


# # Keep ModelBackend around for per-user permissions and maybe a local
# # superuser.
AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)
