# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backoffice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lieu',
            name='photos',
            field=models.ManyToManyField(through='backoffice.PhotoLieu', to='backoffice.Photo'),
        ),
        migrations.AlterField(
            model_name='appuser',
            name='picture',
            field=models.ImageField(blank=True, default='media/avatar.jpg', null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='lieu',
            name='mainPhoto',
            field=models.ImageField(blank=True, default='media/avatarlieux.jpg', null=True, upload_to='media'),
        ),
    ]
