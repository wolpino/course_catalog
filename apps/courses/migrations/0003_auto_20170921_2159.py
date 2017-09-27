# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 21:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20170921_2116'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='courses.Course')),
            ],
        ),
        migrations.RemoveField(
            model_name='desc',
            name='course_id',
        ),
        migrations.AddField(
            model_name='desc',
            name='course',
            field=models.OneToOneField(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='description', to='courses.Course'),
            preserve_default=False,
        ),
    ]