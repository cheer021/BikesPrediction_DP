# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('station_id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('latitude', models.DecimalField(max_digits=15, decimal_places=12)),
                ('longtitude', models.DecimalField(max_digits=15, decimal_places=12)),
            ],
        ),
        migrations.CreateModel(
            name='StationDataNow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datetime', models.DateTimeField(verbose_name=b'time now')),
                ('last_comm_with_server', models.DateTimeField(verbose_name=b'last communication with server')),
                ('nb_bikes', models.IntegerField()),
                ('nb_empty_docks', models.IntegerField()),
                ('station', models.ForeignKey(to='bikesmtl.Station')),
            ],
        ),
    ]
