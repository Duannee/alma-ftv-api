# Generated by Django 5.1.4 on 2025-01-16 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_alter_student_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='email',
        ),
        migrations.RemoveField(
            model_name='student',
            name='name',
        ),
    ]
