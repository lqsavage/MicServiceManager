# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-04 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='env',
            name='image_domain',
            field=models.CharField(default='11', max_length=64),
        ),
        migrations.AddField(
            model_name='env',
            name='image_project',
            field=models.CharField(default='lufeng-test', max_length=32),
        ),
        migrations.AddField(
            model_name='envconfigparams',
            name='status',
            field=models.CharField(default='0', max_length=1),
        ),
        migrations.AddField(
            model_name='micserviceconfigparams',
            name='status',
            field=models.CharField(default='0', max_length=1),
        ),
        migrations.AlterField(
            model_name='env',
            name='gitlab_branch',
            field=models.CharField(max_length=32),
        ),
    ]
