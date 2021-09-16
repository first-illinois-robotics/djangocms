from .common import *

if os.environ.get("GOOGLE_CLOUD_PROJECT", None):
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
