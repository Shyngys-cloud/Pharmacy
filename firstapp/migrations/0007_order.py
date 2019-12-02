# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-24 14:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('firstapp', '0006_auto_20191112_0045'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=255)),
                ('buying_type', models.CharField(choices=[('Go', 'Go'), ('Dost', 'Dost')], max_length=40)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('comments', models.TextField()),
                ('status', models.CharField(choices=[('Accepted for processing', 'Accepted for processing'), ('Performed', 'Performed'), ('Paid', 'Paid')], max_length=100)),
                ('items', models.ManyToManyField(to='firstapp.Cart')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
