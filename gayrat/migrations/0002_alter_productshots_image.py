# Generated by Django 4.2 on 2023-05-01 16:02

from django.db import migrations, models
import gayrat.instances


class Migration(migrations.Migration):

    dependencies = [
        ("gayrat", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productshots",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to=gayrat.instances.get_shots_path
            ),
        ),
    ]
