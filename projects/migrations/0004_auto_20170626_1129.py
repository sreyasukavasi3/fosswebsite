# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 11:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20170624_1257'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProjectImages',
            new_name='ProjectScreenShot',
        ),
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='project/'),
        ),
    ]
