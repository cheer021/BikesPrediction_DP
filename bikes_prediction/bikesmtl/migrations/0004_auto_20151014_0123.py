# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikesmtl', '0003_auto_20151013_2357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stationdatanow',
            name='station_id',
        ),
        migrations.AddField(
            model_name='stationdatanow',
            name='station',
            field=models.OneToOneField(primary_key=True, default=-1, serialize=False, to='bikesmtl.Station'),
        ),
    ]
