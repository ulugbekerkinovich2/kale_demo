# Generated by Django 4.2 on 2023-04-30 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0011_rename_description_product_description_en_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gallerydata1',
            old_name='text',
            new_name='text_en',
        ),
        migrations.RenameField(
            model_name='gallerydata1',
            old_name='title',
            new_name='text_ru',
        ),
        migrations.AddField(
            model_name='gallerydata1',
            name='text_uz',
            field=models.TextField(blank=True, default='matn kiritilmagan', null=True),
        ),
        migrations.AddField(
            model_name='gallerydata1',
            name='title_en',
            field=models.TextField(blank=True, default='matn kiritilmagan', null=True),
        ),
        migrations.AddField(
            model_name='gallerydata1',
            name='title_ru',
            field=models.TextField(blank=True, default='matn kiritilmagan', null=True),
        ),
        migrations.AddField(
            model_name='gallerydata1',
            name='title_uz',
            field=models.TextField(blank=True, default='matn kiritilmagan', null=True),
        ),
    ]
