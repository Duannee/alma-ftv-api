# Generated by Django 5.1.4 on 2025-02-04 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0010_alter_student_frequency_of_classes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='profile_img',
            field=models.TextField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
