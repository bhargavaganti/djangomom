# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-01-01 13:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_signup_is_ready'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='signup',
            options={'ordering': ['-created_at']},
        ),
    ]