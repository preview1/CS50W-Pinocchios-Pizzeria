# Generated by Django 2.2 on 2019-04-06 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0026_auto_20190406_0536'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_state',
            name='value',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
