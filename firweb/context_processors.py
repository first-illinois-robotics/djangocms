from django.conf import settings


def analytics_tag(request):
    return {"GOOGLE_MEASUREMENT_ID": settings.GOOGLE_MEASUREMENT_ID}
