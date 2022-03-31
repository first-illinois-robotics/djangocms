from aldryn_apphooks_config.admin import BaseAppHookConfig
from cms.admin.placeholderadmin import PlaceholderAdminMixin
from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(League)


class HideSidebarMixin:
    # hide in the side bar if just needs to be editable elsewhere
    def has_module_permission(self, request):
        return False


@admin.register(GlobalSeason)
class GlobalSeasonAdmin(HideSidebarMixin, admin.ModelAdmin):
    pass


@admin.register(RegularEvent)
class RegularEventAdmin(HideSidebarMixin, admin.ModelAdmin):
    pass


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    pass


class TeamYearAdmin(PlaceholderAdminMixin, admin.StackedInline):
    model = TeamYear
    extra = 0


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    inlines = [
        TeamYearAdmin
    ]


class EventPageAdmin(PlaceholderAdminMixin, admin.TabularInline):
    model = EventPage
    extra = 0


class AwardAdmin(PlaceholderAdminMixin, admin.TabularInline):
    model = Award
    extra = 0


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [
        EventPageAdmin,
        AwardAdmin
    ]


@admin.register(EventConfig)
class EventConfigAdmin(HideSidebarMixin, BaseAppHookConfig, admin.ModelAdmin):
    pass


@admin.register(RegularEventConfig)
class RegularEventConfigAdmin(HideSidebarMixin, BaseAppHookConfig, admin.ModelAdmin):
    pass
