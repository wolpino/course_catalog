# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 21:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Desc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='desc',
        ),
        migrations.AddField(
            model_name='desc',
            name='course_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='description_id', to='courses.Course'),
        ),
    ]
