from __future__ import annotations

from typing import Type
from django.http import HttpRequest
from cms.apphook_pool import apphook_pool
from django.urls import resolve

from ..models import Event, RegularEvent

from events.competitions import Competition


def get_apphook_conf(request: HttpRequest):
    app = apphook_pool.get_apphook(request.current_page.application_urls)
    app.get_config()
    namespace = resolve(request.path_info).namespace
    return app.get_config(namespace)


def event_index_view(request: HttpRequest):
    event: Event = get_apphook_conf(request)


def event_page_view(request: HttpRequest, slug: str = None):
    pass


def team_list_view(request: HttpRequest, program: Competition):
    pass


def event_list_view(request: HttpRequest, program: Competition):
    pass
