# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rc', '0010_players_attempt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='players',
            name='attempt',
        ),
    ]
