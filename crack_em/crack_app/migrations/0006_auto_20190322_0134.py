# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-22 01:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crack_app', '0005_auto_20190322_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(max_length=128, unique=True),
        ),
    ]
