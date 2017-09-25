# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pname1', models.CharField(max_length=100, null=True, blank=True)),
                ('phone1', models.CharField(max_length=100)),
                ('email1', models.EmailField(max_length=100)),
                ('pname2', models.CharField(max_length=100)),
                ('phone2', models.CharField(max_length=100)),
                ('email2', models.EmailField(max_length=100)),
                ('level', models.IntegerField(default=0)),
                ('total_score', models.IntegerField(default=0)),
                ('user', models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Qattempt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.TextField(max_length=1000000)),
                ('correct_option', models.CharField(max_length=1)),
                ('level', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='qattempt',
            name='question',
            field=models.ForeignKey(to='rc.Question'),
        ),
        migrations.AddField(
            model_name='qattempt',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
