import logging
import requests
from django.http import HttpRequest

from ..decorators import require_gae_cron
from . import FRC_BASE_URL


@require_gae_cron
def get_frc_seasons(request: HttpRequest):
    api_index = requests.request("GET", FRC_BASE_URL).json()
    logging.info(api_index)
