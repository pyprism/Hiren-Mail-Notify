# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-28 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0008_book_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='folder',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]