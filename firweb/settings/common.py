import os  # isort:skip

gettext = lambda s: s
DATA_DIR = os.path.dirname(os.path.dirname(__file__))
"""
Django settings for firweb project.

Generated by 'django-admin startproject' using Django 3.1.11.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

ALLOWED_HOSTS = []

ROOT_URLCONF = "firweb.urls"

WSGI_APPLICATION = "firweb.wsgi.application"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en"

TIME_ZONE = "America/Chicago"

USE_L10N = True

USE_TZ = True

USE_I18N = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = "/static/"
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(DATA_DIR, "media")
STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "theme", "dist"),
    os.path.join(BASE_DIR, "firweb", "static"),
)

SITE_ID = 1


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "firweb", "templates"),
        ],
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.template.context_processors.media",
                "django.template.context_processors.csrf",
                "django.template.context_processors.tz",
                "sekizai.context_processors.sekizai",
                "django.template.context_processors.static",
                "cms.context_processors.cms_settings",
            ],
            "loaders": [
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
        },
    },
]


MIDDLEWARE = [
    "cms.middleware.utils.ApphookReloadMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "cms.middleware.user.CurrentUserMiddleware",
    "cms.middleware.page.CurrentPageMiddleware",
    "cms.middleware.toolbar.ToolbarMiddleware",
    "cms.middleware.language.LanguageCookieMiddleware",
]

INSTALLED_APPS = [
    "djangocms_admin_style",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.admin",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django.contrib.staticfiles",
    "django.contrib.messages",
    "cms",
    "menus",
    "sekizai",
    "treebeard",
    "djangocms_text_ckeditor",
    "filer",
    "easy_thumbnails",
    "djangocms_bootstrap5",
    "djangocms_bootstrap5.contrib.bootstrap5_alerts",
    "djangocms_bootstrap5.contrib.bootstrap5_badge",
    "djangocms_bootstrap5.contrib.bootstrap5_card",
    "djangocms_bootstrap5.contrib.bootstrap5_carousel",
    "djangocms_bootstrap5.contrib.bootstrap5_collapse",
    "djangocms_bootstrap5.contrib.bootstrap5_content",
    "djangocms_bootstrap5.contrib.bootstrap5_grid",
    "djangocms_bootstrap5.contrib.bootstrap5_jumbotron",
    "djangocms_bootstrap5.contrib.bootstrap5_link",
    "djangocms_bootstrap5.contrib.bootstrap5_listgroup",
    "djangocms_bootstrap5.contrib.bootstrap5_media",
    "djangocms_bootstrap5.contrib.bootstrap5_picture",
    "djangocms_bootstrap5.contrib.bootstrap5_tabs",
    "djangocms_bootstrap5.contrib.bootstrap5_utilities",
    "djangocms_file",
    "djangocms_icon",
    "djangocms_link",
    "djangocms_picture",
    "djangocms_style",
    "djangocms_googlemap",
    "djangocms_video",
    "firweb",
]

CMS_TEMPLATES = (("fullwidth.html", "Fullwidth"),)

X_FRAME_OPTIONS = "SAMEORIGIN"

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}

THUMBNAIL_PROCESSORS = (
    "easy_thumbnails.processors.colorspace",
    "easy_thumbnails.processors.autocrop",
    "filer.thumbnail_processors.scale_and_crop_with_subject_location",
    "easy_thumbnails.processors.filters",
)

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
