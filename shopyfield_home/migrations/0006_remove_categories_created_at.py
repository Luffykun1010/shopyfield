# Generated by Django 4.2.5 on 2023-11-05 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopyfield_home', '0005_categories_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='created_at',
        ),
    ]