# Generated by Django 2.2 on 2019-04-30 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0057_auto_20190430_1104'),
    ]

    operations = [
        migrations.RenameField(
            model_name='single_order_item',
            old_name='order1',
            new_name='order',
        ),
        migrations.RemoveField(
            model_name='order',
            name='temp',
        ),
    ]
