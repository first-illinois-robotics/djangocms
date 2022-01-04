from django.http import HttpResponse
from haystack.management.commands import update_index  # type: ignore


def handle_startup(request):
    # since we're using whoosh with a directory of /tmp we have to rebuild the search index on startup
    # not entirely ideal but beats having to run a ES instance
    # GAE blocks users from the /_ah/ URLs so we don't have to worry about someone calling this externally
    cmd = update_index.Command()
    cmd.handle()
    return HttpResponse(status=200)
