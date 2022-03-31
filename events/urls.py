from django.urls import path

from .views import scrapers

urlpatterns = [
    path("seasons/frc/", scrapers.get_frc_seasons),
]
