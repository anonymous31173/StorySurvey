# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-04 23:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0006_auto_20160404_2342'),
    ]

    operations = [
        migrations.AddField(
            model_name='storyevent',
            name='order',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]