# Generated by Django 2.2 on 2019-04-30 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0051_single_order_item2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='single_order_item2',
            old_name='order',
            new_name='order1',
        ),
        migrations.AddField(
            model_name='order',
            name='temp',
            field=models.ManyToManyField(to='orders.Single_Order_Item2'),
        ),
    ]