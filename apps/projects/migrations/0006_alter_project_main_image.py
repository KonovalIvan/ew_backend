# Generated by Django 4.1.6 on 2023-11-18 14:36

from django.db import migrations, models

import apps.base_services


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0005_delete_projectgallery"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="main_image",
            field=models.ImageField(
                blank=True, null=True, upload_to=apps.base_services.generate_random_filename_for_project
            ),
        ),
    ]
