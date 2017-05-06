# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from TriggerWarnings import trigger_types

# Create your models here.

#trigger_types could be in a separate file that gets imported ... that
#way you wouldn't have to worry about keeping the list sync'd between
#the users db and the movies db ... but for now, this is fine
#trigger_types = [ ('t1', 'Animal Cruelty'), ('t2', 'It was all a dream'), ('t3', 'He/She was dead all along'), ('t4', 'Main character dies'), ('t5', 'Cliff Hanger Ending'), ('t6', 'Cliff Hanger Ending without sequel') ]
#triggers = {}
#for type in trigger_types:
#    Profiles.add_to_class(
#    triggers[type] = models.BooleanField(default=False, verbose_name=type)


# List of triggers
#class Triggers(models.Model):
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
                              unique = True)
    password = models.CharField(max_length=100,
                                help_text="Keep it under 100 characters")
    for trigger, descr in trigger_types.types:
        locals()[trigger] = models.BooleanField(default=False, verbose_name=descr)

    del locals()['trigger']

#    triggers = models.ForeignKey(Triggers)


