# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-26 12:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_date_added'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=75)),
                ('content', models.CharField(max_length=250)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('views', models.IntegerField(default=0)),
                ('useful', models.IntegerField(default=0)),
                ('comment_on', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Product_Comment', to='products.Product')),
            ],
        ),
    ]