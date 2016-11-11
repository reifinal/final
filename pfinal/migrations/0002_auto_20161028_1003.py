# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfinal', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='matricula',
            old_name='pelicula',
            new_name='curso',
        ),
        migrations.RenameField(
            model_name='matricula',
            old_name='actor',
            new_name='estudiante',
        ),
    ]
