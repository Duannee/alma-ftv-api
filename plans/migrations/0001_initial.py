# Generated by Django 5.1.3 on 2024-12-05 18:01

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0006_alter_student_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentPlans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_day', models.IntegerField()),
                ('weekly_frequency', models.CharField(choices=[('1X', '1X'), ('2X', '2X'), ('3X', '3X'), ('4X', '4X'), ('5X', '5X')], max_length=2)),
                ('type_plan', models.CharField(choices=[('QUARTERLY', 'QUARTERLY'), ('SEMIANNUAL', 'SEMIANNUAL')], max_length=10)),
                ('value', models.DecimalField(decimal_places=2, max_digits=7)),
                ('status', models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('INACTIVE', 'INACTIVE')], max_length=8)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_plans', to='students.student')),
            ],
        ),
    ]
