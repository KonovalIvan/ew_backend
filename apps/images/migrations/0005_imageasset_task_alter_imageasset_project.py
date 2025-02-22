# Generated by Django 4.1.6 on 2023-11-29 15:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("particular_task", "0004_remove_task_photo_alter_task_dashboard"),
        ("projects", "0006_alter_project_main_image"),
        ("images", "0004_alter_imageasset_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="imageasset",
            name="task",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="image_gallery",
                to="particular_task.task",
            ),
        ),
        migrations.AlterField(
            model_name="imageasset",
            name="project",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="image_gallery",
                to="projects.project",
            ),
        ),
    ]
