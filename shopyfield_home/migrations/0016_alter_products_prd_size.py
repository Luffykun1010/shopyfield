# Generated by Django 4.2.5 on 2024-01-06 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopyfield_home', '0015_products_prd_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='prd_size',
            field=models.CharField(max_length=200),
        ),
    ]
