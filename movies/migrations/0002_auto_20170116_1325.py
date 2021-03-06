# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-16 13:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='actors',
            new_name='actor',
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='director', to='movies.Person'),
        ),
    ]
