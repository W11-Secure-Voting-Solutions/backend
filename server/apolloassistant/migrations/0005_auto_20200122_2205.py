# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-01-22 22:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helios_auth', '0001_initial'),
        ('apolloassistant', '0004_auto_20200122_2145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='castcode',
            name='session_id',
        ),
        migrations.RemoveField(
            model_name='lockincode',
            name='session_id',
        ),
        migrations.AddField(
            model_name='castcode',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='helios_auth.User'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lockincode',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='helios_auth.User'),
            preserve_default=False,
        ),
    ]