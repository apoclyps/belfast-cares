# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-10 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisation',
            name='just_giving_link',
            field=models.CharField(blank=True, max_length=255, verbose_name='just_giving_link'),
        ),
    ]
