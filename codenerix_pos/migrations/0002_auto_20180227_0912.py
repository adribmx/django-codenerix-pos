# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-27 08:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codenerix_pos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pos',
            name='hardware',
            field=models.ManyToManyField(blank=True, related_name='poss', to='codenerix_pos.POSHardware', verbose_name='Hardware it can use'),
        ),
        migrations.AlterField(
            model_name='pos',
            name='storage_query',
            field=models.ManyToManyField(blank=True, related_name='poss_storage_query', to='codenerix_storages.Storage', verbose_name='Storages where you can consult'),
        ),
        migrations.AlterField(
            model_name='pos',
            name='storage_stock',
            field=models.ManyToManyField(blank=True, related_name='poss_storage_stock', to='codenerix_storages.Storage', verbose_name='Storages where the stock is subtracted'),
        ),
    ]
