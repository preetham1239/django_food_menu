# Generated by Django 3.2.12 on 2023-04-05 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='item_price',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
    ]
