# Generated by Django 2.2 on 2019-04-30 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0058_auto_20190430_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='single_order_item',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='in_order', to='orders.Order'),
        ),
    ]
