# Generated by Django 2.2 on 2019-04-05 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0019_auto_20190404_1334'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='toppings',
            new_name='toppings_type',
        ),
    ]
