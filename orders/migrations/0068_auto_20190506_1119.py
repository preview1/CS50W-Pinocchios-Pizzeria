# Generated by Django 2.2.1 on 2019-05-06 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0067_menu_show'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='comment',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
