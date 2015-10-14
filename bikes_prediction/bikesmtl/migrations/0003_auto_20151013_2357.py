# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikesmtl', '0002_auto_20151013_2335'),
    ]

    operations = [
        migrations.RenameField(
            model_name='station',
            old_name='longtitude',
            new_name='longitude',
        ),
    ]
