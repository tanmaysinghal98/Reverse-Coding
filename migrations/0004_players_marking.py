# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rc', '0003_auto_20160906_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='players',
            name='marking',
            field=models.IntegerField(default=4),
        ),
    ]
