# Generated by Django 4.2 on 2023-04-25 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0002_about_best_seller_products_catalog_category_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
