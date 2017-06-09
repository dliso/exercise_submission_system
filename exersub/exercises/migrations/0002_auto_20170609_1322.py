# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-09 13:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='title',
            field=models.CharField(default='Boop beep', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='creation_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 6, 9, 13, 22, 28, 141614, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='creation_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 6, 9, 13, 22, 28, 142202, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='group',
            name='creation_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 6, 9, 13, 22, 28, 139669, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='handin',
            name='handin_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 6, 9, 13, 22, 28, 140881, tzinfo=utc)),
        ),
    ]