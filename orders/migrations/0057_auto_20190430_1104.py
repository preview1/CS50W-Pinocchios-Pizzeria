# Generated by Django 2.2 on 2019-04-30 11:04

from django.db import migrations


class Migration(migrations.Migration):
    
    atomic = False

    dependencies = [
        ('orders', '0056_delete_single_order_item'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Single_Order_Item2',
            new_name='Single_Order_Item',
        ),
    ]
