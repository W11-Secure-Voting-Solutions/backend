# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-01-21 12:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helios', '0003_voter_session_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='voter',
            name='qr_code',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='voter',
            name='session_id',
            field=models.TextField(default=''),
        ),
    ]