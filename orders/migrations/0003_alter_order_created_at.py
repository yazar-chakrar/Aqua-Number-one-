# Generated by Django 4.1.1 on 2022-09-26 20:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_order_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 26, 21, 0, 41, 146190), verbose_name='Ordred at'),
        ),
    ]
