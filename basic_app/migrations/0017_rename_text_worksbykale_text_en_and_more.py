# Generated by Django 4.2 on 2023-04-30 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0016_rename_text_location_text_en_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='worksbykale',
            old_name='text',
            new_name='text_en',
        ),
        migrations.RenameField(
            model_name='worksbykale',
            old_name='title',
            new_name='title_en',
        ),
        migrations.AddField(
            model_name='worksbykale',
            name='text_ru',
            field=models.TextField(blank=True, default='matn kiritilmagan', null=True),
        ),
        migrations.AddField(
            model_name='worksbykale',
            name='text_uz',
            field=models.TextField(blank=True, default='matn kiritilmagan', null=True),
        ),
        migrations.AddField(
            model_name='worksbykale',
            name='title_ru',
            field=models.CharField(blank=True, default='matn kiritilmagan', max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='worksbykale',
            name='title_uz',
            field=models.CharField(blank=True, default='matn kiritilmagan', max_length=512, null=True),
        ),
    ]
