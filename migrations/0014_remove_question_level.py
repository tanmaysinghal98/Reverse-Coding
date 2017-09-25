# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rc', '0013_auto_20160909_0042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='level',
        ),
    ]
