# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-19 23:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_auto_20170909_0924'),
    ]

    operations = [
        migrations.CreateModel(
            name='Backup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('content', models.TextField()),
                ('key', models.TextField()),
                ('sender', models.TextField()),
            ],
        ),
    ]
