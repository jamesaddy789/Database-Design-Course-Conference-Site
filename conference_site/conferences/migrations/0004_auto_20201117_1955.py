# Generated by Django 3.1.3 on 2020-11-18 01:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0003_auto_20201117_1728'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='materials',
            options={'verbose_name_plural': 'Materials'},
        ),
        migrations.AlterField(
            model_name='bill',
            name='current_balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='bill',
            name='payment_type',
            field=models.CharField(choices=[(0, 'credit card'), (1, 'cash'), (2, 'check')], default=(0, 'credit card'), max_length=100),
        ),
        migrations.AlterField(
            model_name='conference',
            name='name',
            field=models.CharField(default='Conference', max_length=200),
        ),
        migrations.AlterField(
            model_name='conference_date',
            name='date_time',
            field=models.DateTimeField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='materials',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='materials',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=5, max_digits=10),
        ),
        migrations.AlterField(
            model_name='materials',
            name='material_type',
            field=models.CharField(choices=[(0, 'banquet ticket'), (1, 'proceedings')], default=(0, 'banquet ticket'), max_length=50),
        ),
        migrations.AlterField(
            model_name='session',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=10),
        ),
        migrations.AlterField(
            model_name='session',
            name='discount_deadline',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='session',
            name='number_of_registrants',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='session',
            name='number_of_speakers',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='session',
            name='session_type',
            field=models.CharField(choices=[(2, 'workshop'), (1, 'tutorial'), (0, 'technical')], default=(2, 'workshop'), max_length=10),
        ),
        migrations.AlterField(
            model_name='session',
            name='title',
            field=models.CharField(default='Title', max_length=200),
        ),
    ]
