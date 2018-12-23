# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alarm',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200, blank=True, null=True)),
                ('message', models.CharField(max_length=2048, blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=10, default='NONE', choices=[('new', 'NEW'), ('checked', 'CHECKED')])),
            ],
        ),
    ]
