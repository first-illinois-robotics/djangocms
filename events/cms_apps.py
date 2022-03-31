from aldryn_apphooks_config.app_base import CMSConfigApp
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.urls import re_path, path
from .models import Event, RegularEvent
from .views.app import app_index_view, app_page_view
from .competitions import Competition


@apphook_pool.register
class EventApp(CMSConfigApp):
    name = "Single Event Listing"
    app_name = "event"
    app_config = Event

    def get_urls(self, page=None, language=None, **kwargs):
        return [
            re_path(r'^$', app_index_view, name='index'),
            path("<slug:slug>/", app_page_view, name='page')
        ]


@apphook_pool.register
class RegularEventApp(CMSConfigApp):
    name = "Regular Event Listing"
    app_name = "regular_event"
    app_config = RegularEvent

    def get_urls(self, page=None, language=None, **kwargs):
        return [
            re_path(r'^$', app_index_view, name='index'),
            path("<slug:slug>/", app_page_view, name='page')
        ]


class GenericTeamApp(CMSApp):
    app_name = "team"
    program = Competition.UNKNOWN

    def __init__(self):
        self.name = f"{self.program} Team Listing"

    def get_urls(self, page=None, language=None, **kwargs):
        return [
            re_path(r'^$', app_index_view, name='index'),
            path("<slug:slug>/", app_page_view, name='page')
        ]


@apphook_pool.register
class FRCTeamsApp(GenericTeamApp):
    program = Competition.FRC


@apphook_pool.register
class FTCTeamsApp(GenericTeamApp):
    program = Competition.FTC


@apphook_pool.register
class FLLCTeamsApp(GenericTeamApp):
    program = Competition.FLLC


@apphook_pool.register
class FLLETeamsApp(GenericTeamApp):
    program = Competition.FLLE