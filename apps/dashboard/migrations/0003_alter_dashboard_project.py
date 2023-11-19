# Generated by Django 4.1.6 on 2023-10-23 17:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0003_delete_buildingproject_projectgallery_project_and_more"),
        ("dashboard", "0002_alter_dashboard_project"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dashboard",
            name="project",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="dashboard",
                to="projects.project",
            ),
        ),
    ]
