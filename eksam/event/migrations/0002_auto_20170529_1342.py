# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 10:42
from __future__ import unicode_literals

from django.db import migrations, models
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='position',
            field=geoposition.fields.GeopositionField(default=geoposition.fields.GeopositionField(max_length=42, verbose_name=52.522906), max_length=42),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(max_length=100),
        ),
    ]