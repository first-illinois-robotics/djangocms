from django.db import models


class Competition(models.TextChoices):
    UNKNOWN = "UK", "Unknown"
    FRC = "FRC", "FIRST Robotics Competition"
    FTC = "FTC", "FIRST Tech Challenge"
    FLLC = "FLLC", "FIRST LEGO League Challenge"
    FLLE = "FLLE", "FIRST LEGO League Explore"
    FLLD = "FLLD", "FIRST LEGO League Discover"
