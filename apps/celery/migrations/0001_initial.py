# Generated by Django 4.1.6 on 2024-01-09 18:42

import uuid

import django.core.serializers.json
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CeleryTask",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("task_name", models.TextField(max_length=256)),
                ("task_args", models.JSONField(blank=True, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ("task_kwargs", models.JSONField(blank=True, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ("task_eta", models.DateTimeField()),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
