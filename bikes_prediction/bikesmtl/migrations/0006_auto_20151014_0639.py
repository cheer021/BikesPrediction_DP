# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bikesmtl', '0005_auto_20151014_0132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stationdatanow',
            name='datetime',
        ),
        migrations.AddField(
            model_name='station',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 14, 6, 39, 10, 153481, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stationdatanow',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 14, 6, 39, 20, 456420, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='station',
            name='station_id',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='stationdatanow',
            name='station',
            field=models.ForeignKey(primary_key=True, serialize=False, to='bikesmtl.Station'),
        ),
    ]
