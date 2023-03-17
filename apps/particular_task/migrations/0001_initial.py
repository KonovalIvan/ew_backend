# Generated by Django 4.1.7 on 2023-03-16 16:04

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("dashboard", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ParticularTask",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=32)),
                ("description", models.TextField()),
                ("status", models.BooleanField(default=False)),
                ("photo", models.ImageField(upload_to="uploads/dashboard/None")),
                (
                    "dashboard",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="task",
                        to="dashboard.projectdashboard",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
