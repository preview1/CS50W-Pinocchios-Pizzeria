# Generated by Django 2.2 on 2019-04-30 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0054_auto_20190430_1032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='dishes',
        ),
    ]
