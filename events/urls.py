from django.urls import path

from .views import scrapers

urlpatterns = [
    path("seasons/frc/", seasons.get_frc_seasons),
]
