# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-26 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoadmin', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='modulelist',
            options={'verbose_name': '\u529f\u80fd\u6a21\u5757'},
        ),
        migrations.AlterModelOptions(
            name='serverappcateg',
            options={'verbose_name': '\u7cfb\u7edf\u96c6\u6210'},
        ),
        migrations.AlterModelOptions(
            name='serverfuncateg',
            options={'verbose_name': '\u670d\u52a1\u529f\u80fd'},
        ),
        migrations.AlterModelOptions(
            name='serverlist',
            options={'verbose_name': '\u670d\u52a1\u4e3b\u673a'},
        ),
        migrations.AlterField(
            model_name='serverlist',
            name='server_lip',
            field=models.GenericIPAddressField(unique=True, verbose_name='\u4e3b\u673a\u5185\u7f51ip'),
        ),
    ]
