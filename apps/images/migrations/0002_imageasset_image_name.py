# Generated by Django 4.1.6 on 2023-11-23 22:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("images", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="imageasset",
            name="image_name",
            field=models.TextField(default=""),
        ),
    ]