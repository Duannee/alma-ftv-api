# Generated by Django 5.1.4 on 2025-01-27 16:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_remove_list_student_id_list_class_time_and_more'),
        ('params', '0002_rename_params_listparams'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='category',
        ),
        migrations.RemoveField(
            model_name='list',
            name='date_day',
        ),
        migrations.AddField(
            model_name='list',
            name='list_params',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='lists', to='params.listparams'),
            preserve_default=False,
        ),
    ]
