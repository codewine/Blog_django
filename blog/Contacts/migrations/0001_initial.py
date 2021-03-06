# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-23 07:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=255)),
                ('subject', models.TextField(blank=True)),
                ('message', models.TextField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
