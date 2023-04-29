# Generated by Django 4.2 on 2023-04-29 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0015_delete_discount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='matn kiritilmagan', max_length=512, null=True)),
                ('phone_number', models.CharField(blank=True, default='matn kiritilmagan', max_length=512, null=True)),
                ('location', models.CharField(blank=True, default='matn kiritilmagan', max_length=512, null=True)),
                ('discount_name', models.CharField(blank=True, default='matn kiritilmagan', max_length=512, null=True)),
                ('total_cost', models.IntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'verbose_name_plural': 'Discount',
            },
        ),
    ]
