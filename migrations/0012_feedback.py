# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rc', '0011_remove_players_attempt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('feedback_question', models.CharField(default=0, max_length=100)),
                ('Excellent', models.CharField(default=0, max_length=100)),
                ('VeryGood', models.CharField(default=0, max_length=100)),
                ('Good', models.CharField(default=0, max_length=100)),
                ('Average', models.CharField(default=0, max_length=100)),
            ],
        ),
    ]
