# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikesmtl', '0004_auto_20151014_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stationdatanow',
            name='station',
            field=models.ForeignKey(primary_key=True, default=-1, serialize=False, to='bikesmtl.Station'),
        ),
    ]
