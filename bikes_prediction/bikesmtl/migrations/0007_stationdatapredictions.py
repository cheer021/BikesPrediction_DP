# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikesmtl', '0006_auto_20151014_0639'),
    ]

    operations = [
        migrations.CreateModel(
            name='StationDataPredictions',
            fields=[
                ('station', models.ForeignKey(primary_key=True, serialize=False, to='bikesmtl.Station')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('nb_bikes_5', models.IntegerField()),
                ('nb_empty_docks_5', models.IntegerField()),
                ('nb_bikes_10', models.IntegerField()),
                ('nb_empty_docks_10', models.IntegerField()),
                ('nb_bikes_15', models.IntegerField()),
                ('nb_empty_docks_15', models.IntegerField()),
                ('nb_bikes_30', models.IntegerField()),
                ('nb_empty_docks_30', models.IntegerField()),
            ],
        ),
    ]
