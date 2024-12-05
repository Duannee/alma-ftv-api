# Generated by Django 5.1.3 on 2024-12-05 18:10

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courts', '0003_alter_court_status'),
        ('lists', '0002_remove_list_student_id_list_class_time_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListCourt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('court', models.ManyToManyField(related_name='list_courts', to='courts.court')),
                ('lists', models.ManyToManyField(related_name='list_courts', to='lists.list')),
            ],
        ),
    ]