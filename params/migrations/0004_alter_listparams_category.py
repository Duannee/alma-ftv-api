# Generated by Django 5.1.4 on 2025-01-27 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('params', '0003_alter_listparams_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listparams',
            name='category',
            field=models.CharField(choices=[('BEGINNER', 'BEGINNER'), ('INTERMEDIARY', 'INTERMEDIARY'), ('ADVANCED', 'ADVANCED'), ('WARNING', 'WARNING'), ('WEEKEND', 'WEEKEND')], max_length=12),
        ),
    ]
