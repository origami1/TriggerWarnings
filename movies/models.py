# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from TriggerWarnings import trigger_types

# Create your models here.

# All we need is a DB for the movies
class Movies(models.Model):
    title = models.CharField(max_length=100,
                             help_text="Keep it under 100 characters, using a release date if needed",
                             unique = True)
    for trigger, descr in trigger_types.types:
        locals()[trigger] = models.BooleanField(default=False, verbose_name=descr)

    del locals()['trigger']
