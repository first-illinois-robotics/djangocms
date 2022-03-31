# Generated by Django 3.2.12 on 2022-03-31 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    # replaces = [
    #     ("events", "0012_auto_20220331_0912"),
    #     ("events", "0013_event_name"),
    #     ("events", "0014_auto_20220331_1010"),
    #     ("events", "0015_auto_20220331_1023"),
    # ]

    dependencies = [
        ("events", "0011_delete_teamconfig"),
        ("cms", "0022_auto_20180620_1551"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="event",
            name="app_config",
        ),
        migrations.RemoveField(
            model_name="regularevent",
            name="app_config",
        ),
        migrations.AddField(
            model_name="season",
            name="name",
            field=models.CharField(default="Unknown", max_length=100, null=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="event",
            name="name",
            field=models.CharField(
                help_text="Do not include the year/season in this, as it will beautomatically added from the season above.",
                max_length=100,
                default="Unknown Event"
            ),
        ),
        migrations.CreateModel(
            name="EventCard",
            fields=[
                (
                    "cmsplugin_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        related_name="events_eventcard",
                        serialize=False,
                        to="cms.cmsplugin",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("cms.cmsplugin",),
        ),
        migrations.DeleteModel(
            name="EventConfig",
        ),
        migrations.DeleteModel(
            name="RegularEventConfig",
        ),
        migrations.AlterField(
            model_name="event",
            name="es02_key",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="event",
            name="lat",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="event",
            name="league",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="events.league",
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="long",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="event",
            name="tba_key",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="event",
            name="teams",
            field=models.ManyToManyField(blank=True, to="events.TeamYear"),
        ),
        migrations.AlterField(
            model_name="event",
            name="toa_key",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name="teamyear",
            name="lat",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="teamyear",
            name="leagues",
            field=models.ManyToManyField(blank=True, to="events.League"),
        ),
        migrations.AlterField(
            model_name="teamyear",
            name="long",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="teamyear",
            name="nickname",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="teamyear",
            name="website",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="eventcard",
            name="event",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="events.event"
            ),
        ),
        migrations.CreateModel(
            name="RegularEventCard",
            fields=[
                (
                    "cmsplugin_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        related_name="events_regulareventcard",
                        serialize=False,
                        to="cms.cmsplugin",
                    ),
                ),
                (
                    "regular_event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="events.regularevent",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("cms.cmsplugin",),
        ),
    ]
