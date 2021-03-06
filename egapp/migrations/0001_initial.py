# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 23:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GraphableFunction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('function_spec', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authors', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('zotero_id', models.IntegerField()),
                ('graphable_functions', models.ManyToManyField(to='egapp.GraphableFunction')),
            ],
        ),
    ]
