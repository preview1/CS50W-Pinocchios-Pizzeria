# Generated by Django 2.2 on 2019-04-29 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0047_menu_in_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='in_order',
        ),
        migrations.AddField(
            model_name='order',
            name='in_order',
            field=models.ManyToManyField(related_name='in_menu', to='orders.Single_Order_Item2'),
        ),
    ]
