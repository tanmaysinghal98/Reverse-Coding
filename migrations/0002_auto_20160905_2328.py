# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='players',
            name='count',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='question',
            name='correct_option',
            field=models.CharField(max_length=100),
        ),
    ]
