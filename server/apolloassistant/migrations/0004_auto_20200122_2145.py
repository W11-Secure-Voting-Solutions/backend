# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-01-22 21:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("helios", "0006_fakebooth"),
        ("apolloassistant", "0003_auto_20200122_2038"),
    ]

    operations = [
        migrations.AddField(
            model_name="castcode",
            name="election",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to="helios.Election",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="lockincode",
            name="election",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                to="helios.Election",
            ),
            preserve_default=False,
        ),
    ]
