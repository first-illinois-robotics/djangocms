# Generated by Django 3.2.12 on 2022-03-31 01:57

import aldryn_apphooks_config.fields
import app_data.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20220326_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100, verbose_name='Type')),
                ('namespace', models.CharField(default=None, max_length=100, unique=True, verbose_name='Instance namespace')),
                ('app_data', app_data.fields.AppDataField(default='{}', editable=False)),
            ],
            options={
                'verbose_name': 'Apphook config',
                'verbose_name_plural': 'Apphook configs',
                'abstract': False,
                'unique_together': {('type', 'namespace')},
            },
        ),
        migrations.AddField(
            model_name='event',
            name='app_config',
            field=aldryn_apphooks_config.fields.AppHookConfigField(help_text='When selecting a value, the form is reloaded to get the updated default', null=True, on_delete=django.db.models.deletion.CASCADE, to='events.eventconfig'),
        ),
    ]
