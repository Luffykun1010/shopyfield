# Generated by Django 4.2.5 on 2023-09-11 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopyfield_home', '0004_cart_order_qty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='prd_rate',
            field=models.IntegerField(),
        ),
    ]
