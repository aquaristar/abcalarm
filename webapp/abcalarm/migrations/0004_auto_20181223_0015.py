# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abcalarm', '0003_auto_20181222_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alarm',
            name='status',
            field=models.CharField(max_length=10, default='new', choices=[('new', 'NEW'), ('checked', 'CHECKED')]),
        ),
    ]
