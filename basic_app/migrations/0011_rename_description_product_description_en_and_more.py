# Generated by Django 4.2 on 2023-04-30 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0010_delete_catalog_delete_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='description',
            new_name='description_en',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='name_en',
        ),
        migrations.AddField(
            model_name='product',
            name='description_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_uz',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_ru',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_uz',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
