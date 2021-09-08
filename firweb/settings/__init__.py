from .common import *

try:
    FIR_ENV = os.environ["FIR_ENV"]
except KeyError:
    print("No valid 'FIR_ENV' environment variable found, assuming 'dev'")
    FIR_ENV = "dev"


if FIR_ENV == "prod":
    # both prod and staging use the same config, the secrets will just import from different projects
    from .prod import *
else:
    INSTALLED_APPS.insert(
        INSTALLED_APPS.index("django.contrib.staticfiles"), "livereload"
    )
    MIDDLEWARE += [
        "livereload.middleware.LiveReloadScript",
    ]
    from .dev import *
