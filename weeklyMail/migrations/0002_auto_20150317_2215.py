# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weeklyMail', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='whole_day',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='end',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='location',
            field=models.CharField(null=True, max_length=255),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='start',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
    ]
