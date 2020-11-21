# Generated by Django 3.1.3 on 2020-11-21 21:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0022_auto_20201121_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conference_date_time',
            name='end_date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 21, 15, 38, 31, 192923)),
        ),
        migrations.AlterField(
            model_name='conference_date_time',
            name='start_date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 21, 15, 38, 31, 192923)),
        ),
        migrations.AlterField(
            model_name='purchased_conference',
            name='transaction_date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 21, 15, 38, 31, 194922)),
        ),
    ]
