# Generated by Django 3.1.3 on 2020-11-19 19:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0011_auto_20201119_1313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conference_date_time',
            name='date_time',
        ),
        migrations.AddField(
            model_name='conference_date_time',
            name='end_date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 19, 13, 19, 31, 535705)),
        ),
        migrations.AddField(
            model_name='conference_date_time',
            name='start_date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 19, 13, 19, 31, 535705)),
        ),
        migrations.AlterField(
            model_name='purchased_material',
            name='transaction_date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 19, 13, 19, 31, 537705)),
        ),
        migrations.AlterField(
            model_name='purchased_session',
            name='transaction_date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 19, 13, 19, 31, 537705)),
        ),
    ]
