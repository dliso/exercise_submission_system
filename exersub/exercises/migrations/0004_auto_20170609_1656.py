# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-09 16:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0003_auto_20170609_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='handin',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='exercises.CUser'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='group',
            name='creation_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='handin',
            name='evaluation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='exercises.Evaluation'),
        ),
        migrations.AlterField(
            model_name='handin',
            name='evaluator_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='evaluator_of', to='exercises.Group'),
        ),
        migrations.AlterField(
            model_name='handin',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='exercises.Group'),
        ),
        migrations.AlterField(
            model_name='handin',
            name='handin_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 6, 9, 16, 56, 21, 373781, tzinfo=utc)),
        ),
    ]