# Generated by Django 4.0.5 on 2022-07-10 15:07

import datetime
from django.db import migrations, models
from datetime import date


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='debt',
            name='interest',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='debt',
            name='paymentDay',
            field=models.CharField(max_length=20),
        ),
        migrations.AddField(
            model_name='debt',
            name='paymentMin',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
        migrations.AddField(
            model_name='debt',
            name='startDate',
            field=models.DateField(default=date.today),
        ),
    ]
