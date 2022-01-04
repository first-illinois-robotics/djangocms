from django.core.exceptions import PermissionDenied
from django.conf import settings
from django.http import HttpRequest


def require_gae_cron(function):
    def wrap(request: HttpRequest, *args, **kwargs):
        if settings.DEBUG or "X-Appengine-Cron" in request.headers:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
