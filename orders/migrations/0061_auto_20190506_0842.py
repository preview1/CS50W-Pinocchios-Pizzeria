# Generated by Django 2.2.1 on 2019-05-06 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0060_auto_20190502_0742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='number_of_toppings',
            field=models.IntegerField(default=0),
        ),
    ]
