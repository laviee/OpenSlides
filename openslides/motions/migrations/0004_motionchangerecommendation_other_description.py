# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-17 10:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motions', '0003_motion_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='motionchangerecommendation',
            name='other_description',
            field=models.TextField(blank=True),
        ),
    ]
