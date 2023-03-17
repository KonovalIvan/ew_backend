# Generated by Django 4.1.7 on 2023-03-16 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0001_initial"),
        ("particular_task", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="particulartask",
            name="assign",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="task",
                to="authentication.user",
            ),
        ),
        migrations.AddField(
            model_name="particulartask",
            name="client_accepting",
            field=models.BooleanField(default=False),
        ),
    ]
