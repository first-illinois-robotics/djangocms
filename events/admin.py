from cms.admin.placeholderadmin import PlaceholderAdminMixin
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(League)


@admin.register(GlobalSeason)
class GlobalSeasonAdmin(admin.ModelAdmin):
    # hide in the side bar (really just need to be edited through Season)
    def has_module_permission(self, request):
        return False


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
