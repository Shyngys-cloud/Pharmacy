# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-10 08:36
from __future__ import unicode_literals

from django.db import migrations, models
import firstapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to=firstapp.models.image_folder),
        ),
    ]