# Generated by Django 4.1.1 on 2022-10-03 19:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0012_alter_food_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 3, 20, 40, 38, 45543), verbose_name='Food Created at'),
        ),
    ]
