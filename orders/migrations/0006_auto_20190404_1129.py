# Generated by Django 2.2 on 2019-04-04 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20190404_1127'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pizzatoppingstypes',
            old_name='numberoftoppings',
            new_name='topping_type',
        ),
    ]
