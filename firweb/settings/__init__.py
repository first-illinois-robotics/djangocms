from .common import *

try:
    FIR_ENV = os.environ["FIR_ENV"]
except KeyError:
    print("No valid 'FIR_ENV' environment variable found, assuming 'dev'")
    FIR_ENV = "dev"


if FIR_ENV == "prod":
    from .prod import *
elif FIR_ENV == "staging":
    from .staging import *
else:
    # INSTALLED_APPS += ("livereload",)
    INSTALLED_APPS.insert(
        INSTALLED_APPS.index("django.contrib.staticfiles"), "livereload"
    )
    MIDDLEWARE += [
        "livereload.middleware.LiveReloadScript",
    ]
    from .dev import *
