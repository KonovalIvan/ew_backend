# Generated by Django 4.1.7 on 2023-03-21 15:04

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0002_rename_projectdashboard_dashboard"),
        ("comments", "0002_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("particular_task", "0002_added_assign_and_accepting_fields"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="ParticularTask",
            new_name="Task",
        ),
    ]
