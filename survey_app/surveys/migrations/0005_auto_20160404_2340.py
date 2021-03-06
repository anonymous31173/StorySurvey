# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-04 23:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0004_auto_20160403_1814'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoryEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text=b'The text of one event in the story.')),
            ],
        ),
        migrations.AlterField(
            model_name='storysurvey',
            name='end',
            field=models.TextField(blank=True, help_text=b'The end of a story that will be provided to the user.'),
        ),
        migrations.AlterField(
            model_name='storysurvey',
            name='start',
            field=models.TextField(blank=True, help_text=b'The beginning of a story that will be provided to the user.'),
        ),
        migrations.AddField(
            model_name='storyevent',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='surveys.StorySurvey'),
        ),
    ]
