# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-18 06:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0002_auto_20171118_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='type',
            field=models.CharField(choices=[('int', 'int'), ('float', 'float'), ('string', 'string'), ('datetime', 'datetime'), ('ip', 'ip')], default='TYPE_STRING', max_length=45),
        ),
    ]