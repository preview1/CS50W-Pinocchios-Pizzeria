# Generated by Django 2.2 on 2019-04-29 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0045_single_order_item_selected_toppings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Single_Order_Item2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selected_toppings', models.CharField(default='None', max_length=128)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Menu')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Order')),
            ],
        ),
    ]
