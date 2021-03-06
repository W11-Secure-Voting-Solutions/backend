# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-01-21 21:34
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("helios", "0005_remove_qrcode"),
    ]

    operations = [
        migrations.CreateModel(
            name="FakeBooth",
            fields=[
                (
                    "id",
                    models.CharField(
                        max_length=100, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("body", django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
    ]
