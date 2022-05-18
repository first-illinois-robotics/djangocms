import os  # isort:skip
from tokenize import String
from typing import List

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

ALLOWED_HOSTS: List[str] = []

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
    os.path.join(BASE_DIR, "frontend", "dist"),
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
                "firweb.context_processors.program",
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
    "django.middleware.cache.UpdateCacheMiddleware",
    "djangocms_redirect.middleware.RedirectMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.common.CommonMiddleware",
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
    "djangocms_redirect",
    "filer",
    "easy_thumbnails",
    "haystack",
    "aldryn_common",
    "aldryn_search",
    "computedfields",
    "standard_form",
    "spurl",
    "gtm",
    "corsheaders",
    "djangocms_file",
    "djangocms_icon",
    "djangocms_frontend",
    "djangocms_frontend.contrib.accordion",
    "djangocms_frontend.contrib.alert",
    "djangocms_frontend.contrib.badge",
    "djangocms_frontend.contrib.card",
    "djangocms_frontend.contrib.carousel",
    "djangocms_frontend.contrib.collapse",
    "djangocms_frontend.contrib.content",
    "djangocms_frontend.contrib.grid",
    "djangocms_frontend.contrib.image",
    "djangocms_frontend.contrib.jumbotron",
    "djangocms_frontend.contrib.link",
    "djangocms_frontend.contrib.listgroup",
    "djangocms_frontend.contrib.media",
    "djangocms_frontend.contrib.tabs",
    "djangocms_frontend.contrib.utilities",
    "djangocms_picture",
    "djangocms_style",
    "djangocms_googlemap",
    "djangocms_video",
    "firweb",
    "events",
]

CMS_TEMPLATES = (("fullwidth.html", "Fullwidth"),)

X_FRAME_OPTIONS = "SAMEORIGIN"


CORS_ALLOWED_ORIGINS = [
    "http://localhost:9001",
    "http://127.0.0.1:8000",
    "https://storage.googleapis.com",
    "https://www.google-analytics.com",
    "https://www.googletagmanager.com",
]


CMS_PERMISSION = True

THUMBNAIL_PROCESSORS = (
    "easy_thumbnails.processors.colorspace",
    "easy_thumbnails.processors.autocrop",
    "filer.thumbnail_processors.scale_and_crop_with_subject_location",
    "easy_thumbnails.processors.filters",
)

# fix for pre django3.2 models
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

HAYSTACK_CONNECTIONS = {
    "default": {
        "ENGINE": "haystack.backends.whoosh_backend.WhooshEngine",
        "PATH": os.path.abspath("/tmp/whoosh/"),
    },
}

# get high-res thumbnails
THUMBNAIL_HIGH_RESOLUTION = True

# allow iframes in text fields
TEXT_ADDITIONAL_TAGS = ("iframe",)
TEXT_ADDITIONAL_ATTRIBUTES = (
    "scrolling",
    "allowfullscreen",
    "frameborder",
    "src",
    "height",
    "width",
)

DJANGOCMS_FRONTEND_CAROUSEL_ASPECT_RATIOS = (
    (16, 9),
    (7, 2),
    (8, 2),
    (9, 2),
    (25, 9),
    (32, 9),
)

DJANGOCMS_FRONTEND_COLOR_STYLE_CHOICES = (
    ("primary", "Primary"),
    ("secondary", "Secondary"),
    ("success", "Success"),
    ("danger", "Danger"),
    ("warning", "Warning"),
    ("info", "Info"),
    ("light", "Light"),
    ("dark", "Dark"),
    ("frc", "FIRST Robotics Competiton"),
    ("ftc", "FIRST Tech Challenge"),
    ("fllc", "FIRST LEGO League Challenge"),
    ("flle", "FIRST LEGO League Explore"),
    ("flld", "FIRST LEGO League Discover"),
)

DJANGOCMS_FRONTEND_ADMIN_CSS = {"all": ("css/cms_admin.css",)}
