from django.conf import settings
from django.http import HttpRequest


def analytics_tag(request: HttpRequest):
    return {"GOOGLE_MEASUREMENT_ID": settings.GOOGLE_MEASUREMENT_ID}


def program(request: HttpRequest):
    ret = {"program": None}
    if request.path.startswith("/frc"):
        ret["program"] = "frc"
    elif request.path.startswith("/ftc"):
        ret["program"] = "ftc"
    elif request.path.startswith("/fll-challenge"):
        ret["program"] = "fllc"
    elif request.path.startswith("/fll-explore"):
        ret["program"] = "flle"
    elif request.path.startswith("/fll-discover"):
        ret["program"] = "flld"
    return ret
