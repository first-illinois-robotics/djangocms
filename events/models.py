from django.db import models


class Competition(models.TextChoices):
    UNKNOWN = "UK", "Unknown"
    FRC = "FRC", "FIRST Robotics Competition"
    FTC = "FTC", "FIRST Tech Challenge"
    FLLC = "FLLC", "FIRST LEGO League Challenge"
    FLLE = "FLLE", "FIRST LEGO League Explore"
    FLLD = "FLLD", "FIRST LEGO League Discover"


class Team(models.Model):
    # This does NOT store team information, just simply a class for everything else to point to
    # You're likely looking for TeamYear down below
    competition = models.IntegerField(
        choices=Competition.choices, default=Competition.UNKNOWN
    )
    team_num = models.IntegerField(null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["team_num", "competition"], name="unique_team"
            )
        ]


class Season(models.Model):
    competition = models.IntegerField(
        choices=Competition.choices, default=Competition.UNKNOWN
    )
    # this year is the same one provided by {FRC/FTC}-Events and/or ES02.
    # May not be exactly the year, since seasons span years
    year = models.IntegerField(null=True)

    # determines if data should still be fetched.
    active = models.BooleanField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["year", "competition"], name="unique_season"
            )
        ]


class League(models.Model):
    code = models.TextField()
    name = models.TextField()
    location = models.TextField()
    season = models.ForeignKey(Season, on_delete=models.PROTECT)
    parentLeague = models.ForeignKey("self", on_delete=models.CASCADE)


class TeamYear(models.Model):
    team = models.ForeignKey(Team, on_delete=models.PROTECT)
    season = models.ForeignKey(Season, on_delete=models.PROTECT)
    leagues = models.ManyToManyField(League)

    nickname = models.TextField(max_length=100, null=True)
    fullname = models.TextField()
    website = models.TextField(null=True)

    city = models.TextField(blank=True)
    state = models.TextField(blank=True)
    country = models.TextField(blank=True)
    lat = models.FloatField(null=True)
    long = models.FloatField(null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["team", "season"], name="unique_team_year")
        ]


class Event(models.Model):
    class TournamentType(models.IntegerChoices):
        # FRC Types
        NoneTournamentType = 0
        Regional = 1
        DistrictEvent = 3  # IL region doesn't have districts but good idea to be able to store them just in case
        DistrictChampionship = 4
        DistrictChampionshipWithLevels = 5
        DistrictChampionshipDivision = 6
        ChampionshipSubdivision = 7
        ChampionshipDivision = 8
        Championship = 9
        OffSeason = 10
        OffSeasonWithAzureSync = 11  # no clue what this is but it's in the docs

        # FTC Types (starting from 100)
        # this is undocumented so these are just gathered from the API responses
        Scrimmage = 100
        LeagueMeet = 101
        Qualifier = 102
        LeagueTournament = 103
        FTCChampionship = 104
        Other = 105
        FTC_FIRSTChampionship = 106
        SuperQualifier = 107
        # 108???
        InnovationChallenge = 109
        FTC_OffSeason = 110

    season = models.ForeignKey(Season, on_delete=models.PROTECT)
    league = models.ForeignKey(League, on_delete=models.PROTECT, null=True)

    # this is the Official event key per FIRST, without the year
    key = models.TextField()

    tournamentType = models.IntegerField(choices=TournamentType.choices)

    start_date = models.DateField()
    end_date = models.DateField()
    lat = models.FloatField(null=True)
    long = models.FloatField(null=True)
    teams = models.ManyToManyField(TeamYear)
