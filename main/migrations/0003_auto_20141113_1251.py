# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20141113_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convenio',
            name='cnpj',
            field=models.CharField(max_length=16, serialize=False, primary_key=True),
        ),
    ]
