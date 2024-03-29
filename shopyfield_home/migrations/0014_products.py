# Generated by Django 4.2.5 on 2024-01-06 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopyfield_home', '0013_remove_categories_sub_cat_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prd_name', models.CharField(max_length=200)),
                ('prd_img', models.ImageField(upload_to='Categories')),
                ('prd_rate', models.IntegerField()),
                ('prd_quantity', models.IntegerField()),
                ('prd_desc', models.CharField(max_length=500)),
                ('seller_company', models.CharField(max_length=200)),
                ('product_code', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('total_sale', models.IntegerField()),
                ('cat_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopyfield_home.categories')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
