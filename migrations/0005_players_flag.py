# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rc', '0004_players_marking'),
    ]

    operations = [
        migrations.AddField(
            model_name='players',
            name='flag',
            field=models.IntegerField(default=1),
        ),
    ]
