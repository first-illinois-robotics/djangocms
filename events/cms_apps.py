from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.core.exceptions import ObjectDoesNotExist
from django.urls import re_path, path, reverse
from .models import Event, RegularEvent
from .views.app import *
from .competitions import Competition


class CMSConfigApp(CMSApp):
    """Taken directly from aldryn-apphooks-config"""

    def get_configs(self):
        return self.app_config.objects.all()

    def get_config(self, namespace):
        try:
            return self.app_config.objects.get(namespace=namespace)
        except ObjectDoesNotExist:
            return None

    def get_config_add_url(self):
        return f"admin:{self.app_config._meta.app_label}_{self.app_config._meta.model_name}_add"


@apphook_pool.register
class EventApp(CMSConfigApp):
    name = "Single Event Listing"
    app_name = "event"
    app_config = Event

    def get_urls(self, page=None, language=None, **kwargs):
        return [
            re_path(r"^$", event_index_view, name="event_index"),
            path("<slug:slug>/", event_page_view, name="event_page"),
        ]


@apphook_pool.register
class RegularEventApp(CMSConfigApp):
    name = "Regular Event Listing"
    app_name = "regular_event"
    app_config = RegularEvent

    def get_urls(self, page=None, language=None, **kwargs):
        return [
            re_path(r"^$", event_index_view, name="index"),
            path("<slug:slug>/", event_page_view, name="page"),
        ]


class GenericTeamApp(CMSApp):
    program = Competition.UNKNOWN
    long_name = ""

    def __init__(self):
        self.name = f"{self.long_name} Team Listing"
        self.app_name = f"{self.program}TeamList"

    def get_urls(self, page=None, language=None, **kwargs):
        return [
            path("", team_list_view, {"program": self.program}, name="team_list"),
        ]


for short_name, long_name in Competition.choices:
    cls = type(f"{short_name}TeamsApp", (GenericTeamApp,), dict(program=short_name, long_name=long_name))
    apphook_pool.register(cls)


class GenericEventListApp(CMSApp):
    program = Competition.UNKNOWN
    long_name = ""

    def __init__(self):
        self.name = f"{self.long_name} Event Listing"
        self.app_name = f"{self.program}EventList"

    def get_urls(self, page=None, language=None, **kwargs):
        return [
            path("", event_list_view, {"program": self.program}, name="team_list"),
        ]


for short_name, long_name in Competition.choices:
    cls = type(f"{short_name}EventsApp", (GenericEventListApp,), dict(program=short_name, long_name=long_name))
    apphook_pool.register(cls)
