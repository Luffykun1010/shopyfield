# Generated by Django 4.2.5 on 2023-10-24 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopyfield_home', '0019_orders_prd_qty_orders_prd_rate_orders_product_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chatbot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('state', models.TextField()),
                ('configuration', models.TextField()),
            ],
        ),
    ]