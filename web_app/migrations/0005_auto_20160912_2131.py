# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-12 21:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0004_auto_20160912_2049'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='wishlists',
        ),
        migrations.AddField(
            model_name='wishlist',
            name='items',
            field=models.ManyToManyField(to='web_app.Item'),
        ),
    ]
