# Generated by Django 5.0.2 on 2024-02-20 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0002_rename_product_products'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]
