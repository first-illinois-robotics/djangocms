# Generated by Django 3.2.12 on 2022-03-27 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20220326_2050'),
    ]

    operations = [
        migrations.AddField(
            model_name='globalseason',
            name='name',
            field=models.TextField(help_text='Season-wide name, like "FIRST Forward"', null=True),
        ),
        migrations.AlterField(
            model_name='award',
            name='individual',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(help_text='Used in URLs'),
        ),
        migrations.AlterField(
            model_name='league',
            name='code',
            field=models.TextField(help_text='Gotten straight from FIRST'),
        ),
        migrations.AlterField(
            model_name='regularevent',
            name='slug',
            field=models.SlugField(help_text='Used in URLs'),
        ),
        migrations.AlterField(
            model_name='season',
            name='active',
            field=models.BooleanField(help_text='Determines if data should still be automatically fetched.'),
        ),
        migrations.AlterField(
            model_name='season',
            name='year',
            field=models.IntegerField(help_text="The year as provided by FIRST's own systems. Generally the yearkickoff is in.", null=True),
        ),
        migrations.AlterField(
            model_name='teamyear',
            name='fullname',
            field=models.TextField(help_text='Full team name including sponsors'),
        ),
    ]
