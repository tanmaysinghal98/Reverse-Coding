# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rc', '0012_feedback'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Feedback',
        ),
        migrations.RemoveField(
            model_name='players',
            name='level',
        ),
    ]
