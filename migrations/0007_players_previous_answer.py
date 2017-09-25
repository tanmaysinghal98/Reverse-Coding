# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rc', '0006_remove_players_flag'),
    ]

    operations = [
        migrations.AddField(
            model_name='players',
            name='previous_answer',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
