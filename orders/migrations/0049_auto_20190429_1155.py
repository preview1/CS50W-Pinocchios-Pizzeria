# Generated by Django 2.2 on 2019-04-29 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0048_auto_20190429_1128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='in_order',
        ),
        migrations.DeleteModel(
            name='Single_Order_Item2',
        ),
    ]
