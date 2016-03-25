# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-03 09:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationmodel',
            name='latitude',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='locationmodel',
            name='longitude',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
    ]
