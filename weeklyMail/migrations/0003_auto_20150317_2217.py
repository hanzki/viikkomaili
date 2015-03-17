# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weeklyMail', '0002_auto_20150317_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='end',
            field=models.DateTimeField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='location',
            field=models.CharField(blank=True, max_length=255, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='start',
            field=models.DateTimeField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
