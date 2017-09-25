# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rc', '0007_players_previous_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='players',
            name='questions_attempted',
            field=models.IntegerField(default=0),
        ),
    ]
