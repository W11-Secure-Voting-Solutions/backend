# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-01-16 18:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("helios", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="QrCode",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("image_base64", models.TextField()),
                (
                    "voter",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="helios.Voter"
                    ),
                ),
            ],
        ),
    ]
