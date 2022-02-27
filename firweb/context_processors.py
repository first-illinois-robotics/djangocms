from django.conf import settings
from django.http import HttpRequest


def analytics_tag(request: HttpRequest):
    return {"GOOGLE_MEASUREMENT_ID": settings.GOOGLE_MEASUREMENT_ID}


def program(request: HttpRequest):
    if request.path.startswith("/frc"):
        return {"program": "frc"}
    elif request.path.startswith("/ftc"):
        return {"program": "ftc"}
    elif request.path.startswith("/fll-challenge"):
        return {"program": "flle"}
    elif request.path.startswith("/fll-explore"):
        return {"program": "flle"}
    elif request.path.startswith("/fll-discover"):
        return {"program": "flld"}
    else:
        return {"program": None}
