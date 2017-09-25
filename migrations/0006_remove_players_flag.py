# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rc', '0005_players_flag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='players',
            name='flag',
        ),
    ]
