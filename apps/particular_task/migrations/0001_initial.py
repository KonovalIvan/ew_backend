# Generated by Django 4.2.4 on 2023-08-18 20:35

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("dashboard", "0001_initial"),
        ("authentication", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Task",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=32)),
                ("description", models.TextField()),
                ("status", models.BooleanField(default=False)),
                ("client_accepting", models.BooleanField(default=False)),
                ("photo", models.ImageField(upload_to="uploads/dashboard/None")),
                (
                    "assign",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="task",
                        to="authentication.user",
                    ),
                ),
                (
                    "dashboard",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="task",
                        to="dashboard.dashboard",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
