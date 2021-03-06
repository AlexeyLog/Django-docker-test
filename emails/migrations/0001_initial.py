# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-04 07:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_id', models.CharField(help_text='Gmail id', max_length=128)),
                ('from_address', models.CharField(max_length=128)),
                ('to_address', models.CharField(max_length=128)),
                ('body', models.TextField()),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]
