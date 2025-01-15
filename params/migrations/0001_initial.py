# Generated by Django 5.1.3 on 2024-12-05 18:36

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Params",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("class_date", models.DateField()),
                ("status", models.BooleanField(default=True)),
                ("expires_at", models.DateTimeField()),
                ("description", models.TextField()),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("BEGINNER", "BEGINNER"),
                            ("INTERMEDIARY", "INTERMEDIARY"),
                            ("ADVANCED", "ADVANCED"),
                        ],
                        max_length=12,
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
