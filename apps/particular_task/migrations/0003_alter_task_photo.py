# Generated by Django 4.1.6 on 2023-11-19 20:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("particular_task", "0002_rename_status_task_finished_task_owner_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="photo",
            field=models.ImageField(blank=True, null=True, upload_to="uploads/dashboard/None"),
        ),
    ]
