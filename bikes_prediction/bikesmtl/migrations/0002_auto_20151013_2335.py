# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikesmtl', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stationdatanow',
            name='id',
        ),
        migrations.RemoveField(
            model_name='stationdatanow',
            name='station',
        ),
        migrations.AddField(
            model_name='stationdatanow',
            name='station_id',
            field=models.IntegerField(default=-1, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='station',
            name='station_id',
            field=models.IntegerField(default=-1, serialize=False, primary_key=True),
        ),
    ]
