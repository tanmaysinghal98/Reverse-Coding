# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rc', '0002_auto_20160905_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='players',
            name='end_time',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='players',
            name='start_time',
            field=models.IntegerField(default=0),
        ),
    ]
