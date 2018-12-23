# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abcalarm', '0002_auto_20181212_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='alarm',
            name='alarm_type',
            field=models.CharField(max_length=10, default='NONE', choices=[('video', 'VIDEO'), ('image', 'IMAGE'), ('attached', 'ATTACHED')]),
        ),
        migrations.AddField(
            model_name='alarm',
            name='url',
            field=models.URLField(max_length=2048, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='alarm',
            name='message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
