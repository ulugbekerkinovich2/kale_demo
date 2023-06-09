# Generated by Django 4.2 on 2023-04-30 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0007_remove_catalog_name_remove_category_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoryproduct',
            old_name='name',
            new_name='name_en',
        ),
        migrations.AddField(
            model_name='categoryproduct',
            name='name_ru',
            field=models.CharField(blank=True, default='matn kiritilmagan', max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='categoryproduct',
            name='name_uz',
            field=models.CharField(blank=True, default='matn kiritilmagan', max_length=512, null=True),
        ),
    ]
