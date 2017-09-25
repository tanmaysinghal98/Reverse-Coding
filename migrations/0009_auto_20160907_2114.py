# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rc', '0008_players_questions_attempted'),
    ]

    operations = [
        migrations.AddField(
            model_name='players',
            name='right_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='players',
            name='wrong_count',
            field=models.IntegerField(default=0),
        ),
    ]
