# Generated by Django 2.2 on 2019-04-12 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0030_auto_20190406_0553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='orders.Order_State'),
        ),
    ]
