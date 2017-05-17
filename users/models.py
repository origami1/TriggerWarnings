# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from TriggerWarnings import trigger_types

# Create your models here.

# List of triggers
#    animal_cruelty = models.BooleanField(default=False)
#    it_was_all_a_dream = models.BooleanField(default=False)
#    she_was_dead_all_along = models.BooleanField(default=False)
#    main_character_dies = models.BooleanField(default=False)
#    cliff_hanger_ending = models.BooleanField(default=False)
#    cliff_hanger_ending_without_sequel = models.BooleanField(default=False)


# All we need is a DB for the users (profiles)
class Profiles(models.Model):
    userid = models.CharField(max_length=100,
                              help_text="Keep it under 100 characters",
                              unique = True,
                              primary_key = True)
    password = models.CharField(max_length=100,
                                help_text="Keep it under 100 characters")
    version = models.IntegerField(default=trigger_types.version)
    for trigger, descr in trigger_types.types:
        locals()[trigger] = models.BooleanField(default=False, verbose_name=descr)

    del locals()['trigger']


