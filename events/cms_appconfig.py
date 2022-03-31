from aldryn_apphooks_config.models import AppHookConfig
from aldryn_apphooks_config.utils import setup_config
from django.db import models
from app_data import AppDataForm
from django import forms

from .competitions import Competition


# Single Event App Hook


class EventConfig(AppHookConfig):
    class Meta:
        verbose_name = 'Single Event Appconfig'


class EventConfigForm(AppDataForm):
    pass


setup_config(EventConfigForm, EventConfig)


# Regular Event App Hook


class RegularEventConfig(AppHookConfig):
    class Meta:
        verbose_name = 'Regular Event Appconfig'


class RegularEventConfigForm(AppDataForm):
    pass


setup_config(RegularEventConfigForm, RegularEventConfig)
