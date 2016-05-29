# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-05-19 18:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('certificate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain_name', models.CharField(max_length=200)),
                ('domain_url', models.CharField(max_length=200)),
                ('domain_registerer', models.CharField(max_length=200)),
                ('support_email', models.CharField(max_length=200)),
                ('top_level_domain', models.CharField(max_length=200)),
                ('date_registered', models.DateField()),
                ('expiration_date', models.DateField()),
                ('last_updated', models.DateField()),
                ('date_entered', models.DateField(auto_now_add=True)),
                ('domain_certificate', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='certified_domain', to='certificate.Certificate')),
            ],
        ),
    ]
