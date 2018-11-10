# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-22 17:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default=django.utils.timezone.now, max_length=120),
            preserve_default=False,
        ),
    ]
