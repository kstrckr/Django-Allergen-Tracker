# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-02 02:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allergens', '0008_auto_20171101_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='edited_on',
            field=models.DateTimeField(null=True),
        ),
    ]