# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-10 01:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=254)),
                ('setnumber', models.DecimalField(decimal_places=0, max_digits=8)),
                ('release_year', models.CharField(default='', max_length=10)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('image1', models.ImageField(upload_to='img')),
                ('image2', models.ImageField(upload_to='img')),
                ('category', models.CharField(default='', max_length=100)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=75)),
                ('content', models.CharField(max_length=250)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('comment_on', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Product_Comment', to='products.Product')),
            ],
        ),
    ]
