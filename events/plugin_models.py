from __future__ import annotations

from cms.models.pluginmodel import CMSPlugin
from django.db import models

__all__ = ["EventCard", "RegularEventCard"]


class EventCard(CMSPlugin):
    event = models.ForeignKey("Event", on_delete=models.PROTECT)

    def copy_relations(self, oldinstance: EventCard):
        self.event = oldinstance.event


class RegularEventCard(CMSPlugin):
    regular_event = models.ForeignKey("RegularEvent", on_delete=models.PROTECT)

    def copy_relations(self, oldinstance: RegularEventCard):
        self.regular_event = oldinstance.regular_event
