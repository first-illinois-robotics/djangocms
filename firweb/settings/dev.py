# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "4nb72wikdf#8t%7o^+1a2shdh%zmk#+w2pod672300c%=xy)h1"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    "default": {
        "CONN_MAX_AGE": 0,
        "ENGINE": "django.db.backends.sqlite3",
        "HOST": "localhost",
        "NAME": "project.db",
        "PASSWORD": "",
        "PORT": "",
        "USER": "",
    }
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
