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
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Season)
class SeasonAdmin(admin.ModelAdmin):
    pass


@admin.register(TeamYear)
class TeamYearAdmin(HideSidebarMixin, admin.ModelAdmin):
    model = TeamYear
    search_fields = ['team__team_num', 'team__competition', 'nickname']


class TeamYearInlineAdmin(admin.StackedInline):
    model = TeamYear
    extra = 0


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    inlines = [
        TeamYearInlineAdmin
    ]


class EventPageAdmin(PlaceholderAdminMixin, admin.TabularInline):
    model = EventPage
    extra = 0
    prepopulated_fields = {"slug": ("title",)}


class AwardAdmin(admin.TabularInline):
    model = Award
    extra = 0


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [
        EventPageAdmin,
        AwardAdmin
    ]
    prepopulated_fields = {"slug": ("name",)}
    autocomplete_fields = ['teams']


