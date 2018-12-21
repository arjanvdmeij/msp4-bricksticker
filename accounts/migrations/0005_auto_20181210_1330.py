# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-10 13:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20181210_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='address1',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='city',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='country',
            field=models.CharField(blank=True, max_length=75),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='postal_code',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
