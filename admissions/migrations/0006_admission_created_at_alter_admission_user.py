# Generated by Django 5.1.4 on 2025-01-15 19:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("admissions", "0005_alter_admission_user"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="admission",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="admission",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="admissions",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
