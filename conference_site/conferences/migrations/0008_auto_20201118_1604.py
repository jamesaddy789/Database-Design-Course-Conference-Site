# Generated by Django 3.1.3 on 2020-11-18 22:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0007_auto_20201118_1341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conference',
            name='number_of_registrants',
        ),
        migrations.RemoveField(
            model_name='session',
            name='discount_deadline',
        ),
        migrations.RemoveField(
            model_name='session',
            name='number_of_registrants',
        ),
        migrations.RemoveField(
            model_name='session',
            name='number_of_speakers',
        ),
        migrations.AddField(
            model_name='conference',
            name='discount_deadline',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='purchased_material',
            name='payment_type',
            field=models.CharField(choices=[('Credit Card', 'Credit Card'), ('Cash', 'Cash'), ('Check', 'Check')], default='Credit Card', max_length=11),
        ),
        migrations.AddField(
            model_name='purchased_session',
            name='payment_type',
            field=models.CharField(choices=[('Credit Card', 'Credit Card'), ('Cash', 'Cash'), ('Check', 'Check')], default='Credit Card', max_length=11),
        ),
        migrations.DeleteModel(
            name='Bill',
        ),
    ]
