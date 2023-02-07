# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2023-01-18 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('mobileno', models.IntegerField(max_length=10)),
                ('query', models.TextField()),
            ],
        ),
    ]
