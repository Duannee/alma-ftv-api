# Generated by Django 5.1.3 on 2024-12-04 17:56

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lists", "0001_initial"),
        ("students", "0006_alter_student_created_at"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="list",
            name="student_id",
        ),
        migrations.AddField(
            model_name="list",
            name="class_time",
            field=models.CharField(
                choices=[
                    ("06:00", "06:00"),
                    ("07:00", "07:00"),
                    ("08:00", "08:00"),
                    ("09:00", "09:00"),
                    ("17:00", "17:00"),
                    ("18:00", "18:00"),
                    ("06:15", "06:15"),
                    ("07:15", "07:15"),
                    ("08:15", "08:15"),
                ],
                default=2,
                max_length=5,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="list",
            name="created_at",
            field=models.DateTimeField(
                default=django.utils.timezone.now, editable=False
            ),
        ),
        migrations.AddField(
            model_name="list",
            name="student",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="lists",
                to="students.student",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="list",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
