# Generated by Django 2.2 on 2019-04-30 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0055_remove_order_dishes'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Single_Order_Item',
        ),
    ]