# Generated by Django 3.0.1 on 2020-01-01 14:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pastebin_app', '0004_auto_20191231_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 1, 14, 50, 6, 588905, tzinfo=utc), verbose_name='Posted date'),
        ),
        migrations.AlterField(
            model_name='paste',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 1, 14, 50, 6, 578888, tzinfo=utc), verbose_name='Creation date'),
        ),
    ]
