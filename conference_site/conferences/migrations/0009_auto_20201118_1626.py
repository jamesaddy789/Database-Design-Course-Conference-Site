# Generated by Django 3.1.3 on 2020-11-18 22:26

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0008_auto_20201118_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conference_Date_Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(default=datetime.datetime(2020, 11, 18, 16, 26, 40, 781208))),
                ('conference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conferences.conference')),
            ],
        ),
        migrations.AlterField(
            model_name='purchased_material',
            name='transaction_date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 18, 16, 26, 40, 783262)),
        ),
        migrations.AlterField(
            model_name='purchased_session',
            name='transaction_date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 18, 16, 26, 40, 783262)),
        ),
        migrations.DeleteModel(
            name='Conference_Date',
        ),
    ]
