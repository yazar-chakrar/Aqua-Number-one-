# Generated by Django 4.1.1 on 2022-10-03 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='persons',
            field=models.IntegerField(default=1, verbose_name='Number of persens'),
        ),
    ]
