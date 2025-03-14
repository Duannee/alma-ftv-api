# Generated by Django 5.1.3 on 2024-12-04 18:07

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("coaches", "0002_coach_profile_img"),
    ]

    operations = [
        migrations.AddField(
            model_name="coach",
            name="created_at",
            field=models.DateTimeField(
                default=django.utils.timezone.now, editable=False
            ),
        ),
        migrations.AddField(
            model_name="coach",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="coach",
            name="phone",
            field=models.CharField(max_length=14),
        ),
    ]
