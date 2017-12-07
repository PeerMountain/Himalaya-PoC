# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-14 00:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ACLRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('messageHash', models.TextField(primary_key=True, serialize=False)),
                ('messageType', models.IntegerField()),
                ('dossierHash', models.TextField()),
                ('bodyHash', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('address', models.TextField(primary_key=True, serialize=False)),
                ('pubkey', models.TextField(unique=True)),
                ('nickname', models.TextField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='acl',
            field=models.ManyToManyField(related_name='incoming_messages', through='API.ACLRule', to='API.Persona'),
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outgoing_messages', to='API.Persona'),
        ),
        migrations.AddField(
            model_name='aclrule',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.Message'),
        ),
        migrations.AddField(
            model_name='aclrule',
            name='reader',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.Persona'),
        ),
    ]
