# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-09 19:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0024_remove_comment_parent_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(max_length=10000),
        ),
    ]
