# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-12 08:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcomment',
            name='content',
            field=models.TextField(max_length=1000),
        ),
    ]
