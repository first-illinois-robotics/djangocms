from django.http import HttpRequest

from events.competitions import Competition


def event_index_view(request: HttpRequest):
    pass


def event_page_view(request: HttpRequest, slug: str = None):
    pass


def team_list_view(request: HttpRequest, program: Competition):
    pass
