# Generated by Django 4.2 on 2023-04-25 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0013_best_seller_products_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.CharField(blank=True, default='mahsulot kodi kiritilmagan', max_length=30, null=True),
        ),
    ]