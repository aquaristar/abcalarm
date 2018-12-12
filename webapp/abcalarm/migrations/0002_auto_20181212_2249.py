# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abcalarm', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alarm',
            old_name='created',
            new_name='created_date',
        ),
    ]
