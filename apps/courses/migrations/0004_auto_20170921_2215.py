# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 22:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20170921_2159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='desc',
            name='id',
        ),
        migrations.AlterField(
            model_name='desc',
            name='course',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='courses.Course'),
        ),
    ]