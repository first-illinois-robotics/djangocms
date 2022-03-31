from cms.models.fields import PlaceholderField
from django.db import models
from .competitions import Competition
from .plugin_models import *


class PageLayoutTypes(models.IntegerChoices):
    """Page layout types for event pages"""
    Tabbed = 0
    Pages = 1


class Team(models.Model):
    # This does NOT store team information, just simply a class for everything else to point to
    # You're likely looking for TeamYear down below
    competition = models.CharField(
        choices=Competition.choices, default=Competition.UNKNOWN, max_length=4
    )
    team_num = models.IntegerField(null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["team_num", "competition"], name="unique_team"
            )
        ]

    def __str__(self):
        return f"{self.competition}{self.team_num}"


class GlobalSeason(models.Model):
    name = models.TextField(help_text="Season-wide name, like \"FIRST Forward\"", null=True)

    def __str__(self):
        return self.name


class Season(models.Model):
    competition = models.CharField(
        choices=Competition.choices, default=Competition.UNKNOWN, max_length=4
    )
    # this year is the same one provided by {FRC/FTC}-Events and/or ES02.
    # May not be exactly the year, since seasons span years
    year = models.IntegerField(null=True, help_text="The year as provided by FIRST's own systems. Generally the year "
                                                    "that kickoff is in.")

    name = models.CharField(max_length=100)

    # the global season should be set for all the seasons happening at the same time
    # i.e. go to te same championship
    global_season = models.ForeignKey(GlobalSeason, on_delete=models.SET_NULL, null=True)

    # determines if data should still be fetched.
    active = models.BooleanField(help_text="Determines if data should still be automatically fetched.")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["year", "competition"], name="unique_season"
            )
        ]

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = f"{self.competition} {self.year} Season"
        super(Season, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class League(models.Model):
    code = models.CharField(help_text="Gotten straight from FIRST", max_length=50)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    season = models.ForeignKey(Season, on_delete=models.PROTECT)
    parentLeague = models.ForeignKey("self", on_delete=models.CASCADE)


class TeamYear(models.Model):
    team = models.ForeignKey(Team, on_delete=models.PROTECT)
    season = models.ForeignKey(Season, on_delete=models.PROTECT)
    leagues = models.ManyToManyField(League, blank=True)

    nickname = models.CharField(max_length=100, null=True, blank=True)
    fullname = models.TextField(help_text="Full team name including sponsors")
    website = models.CharField(null=True, blank=True, max_length=100)

    city = models.CharField(blank=True, max_length=100)
    state = models.CharField(blank=True, max_length=100)
    country = models.CharField(blank=True, max_length=100)
    lat = models.FloatField(null=True, blank=True)
    long = models.FloatField(null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["team", "season"], name="unique_team_year")
        ]

    def __str__(self):
        return f"{self.team} {self.season.name} Season ({self.nickname})"


class RegularEvent(models.Model):
    """For events that happen regularly (i.e. a yearly regional), an easy way of lumping them together"""
    title = models.TextField()
    slug = models.SlugField(help_text="Used in URLs")

    def __str__(self):
        return f"{self.title} ({self.slug})"


class Event(models.Model):
    class TournamentType(models.IntegerChoices):
        # FRC Types
        NoneTournamentType = 0, "FRC None"
        Regional = 1, "FRC Regional"
        DistrictEvent = 3, "FRC District"
        # IL region doesn't have districts but good idea to be able to store them just in case
        DistrictChampionship = 4, "FRC DCMP"
        DistrictChampionshipWithLevels = 5, "FRC DCMP With Levels"
        DistrictChampionshipDivision = 6, "FRC DCMP Sub Division"
        ChampionshipSubdivision = 7, "FRC Champ Subdivision"
        ChampionshipDivision = 8, "FRC Champ Division"
        Championship = 9, "FRC Championship"
        OffSeason = 10, "FRC Offseason"
        OffSeasonWithAzureSync = 11, "FRC Offseason With Azure Sync"  # no clue what this is but it's in the docs

        # FTC Types (starting from 100)
        # this is undocumented so these are just gathered from the API responses
        Scrimmage = 100, "FTC Scrimmage"
        LeagueMeet = 101, "FTC League Meet"
        Qualifier = 102, "FTC Qualifier"
        LeagueTournament = 103, "FTC League Tournament"
        FTCChampionship = 104, "FTC (local) Championship"
        Other = 105, "FTC Other"
        FTC_FIRSTChampionship = 106, "FTC Championship"
        SuperQualifier = 107, "FTC Super Qualifier"
        # 108???
        InnovationChallenge = 109, "FTC Innovation Challenge"
        FTC_OffSeason = 110, "FTC Off Season"

    season = models.ForeignKey(Season, on_delete=models.PROTECT)
    league = models.ForeignKey(League, on_delete=models.PROTECT, null=True, blank=True)
    name = models.CharField(max_length=100, help_text="Do not include the year/season in this, as it will be"
                                                      "automatically added from the season above.")

    slug = models.SlugField(help_text="Used in URLs")

    # this is the Official event key per FIRST, without the year
    official_key = models.CharField(help_text="Official event key from FIRST", max_length=20)
    # alternate keys for third party sites
    es02_key = models.CharField(null=True, blank=True, max_length=20)
    tba_key = models.CharField(null=True, blank=True, max_length=10)
    toa_key = models.CharField(null=True, blank=True, max_length=15)

    tournamentType = models.IntegerField(choices=TournamentType.choices)

    regular_event = models.ForeignKey(RegularEvent, on_delete=models.SET_NULL, null=True,
                                      help_text="Used for a repeating event.")
    start_date = models.DateField()
    end_date = models.DateField()
    lat = models.FloatField(null=True, blank=True)
    long = models.FloatField(null=True, blank=True)
    teams = models.ManyToManyField(TeamYear, blank=True)

    pageType = models.IntegerField(choices=PageLayoutTypes.choices, default=PageLayoutTypes.Tabbed)

    def __str__(self):
        return f"{self.name} ({self.season})"


class Award(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(TeamYear, on_delete=models.PROTECT)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    individual = models.CharField(null=True, help_text="For individual awards like Dean's List", max_length=100)

    def __str__(self):
        return f"{self.name} at {self.event}"


class EventPage(models.Model):
    def get_placeholder_name(self):
        return "content_" + self.slug

    title = models.CharField(max_length=50)
    slug = models.SlugField()
    content = PlaceholderField(get_placeholder_name)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    class PageTypes(models.IntegerChoices):
        Custom = 0
        Teams = 1
        Awards = 2

    pageType = models.IntegerField(choices=PageTypes.choices, default=PageTypes.Custom)

    def __str__(self):
        return self.title
