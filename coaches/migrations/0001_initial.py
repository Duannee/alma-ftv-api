# Generated by Django 5.1.3 on 2024-11-25 19:16

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Coach",
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
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("phone", models.TextField(max_length=20)),
                (
                    "genre",
                    models.CharField(
                        choices=[
                            ("FEMALE", "FEMALE"),
                            ("MALE", "MALE"),
                            ("OTHERS", "OTHERS"),
                        ],
                        max_length=7,
                    ),
                ),
            ],
        ),
    ]
