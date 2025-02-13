# Generated by Django 5.1.4 on 2025-02-13 19:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('params', '0005_listparams_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='listparams',
            name='class_time',
            field=models.TimeField(blank=True, choices=[(datetime.time(6, 0), '06:00'), (datetime.time(7, 0), '07:00'), (datetime.time(8, 0), '08:00'), (datetime.time(9, 0), '09:00'), (datetime.time(17, 0), '17:00'), (datetime.time(18, 0), '18:00'), (datetime.time(6, 15), '06:15'), (datetime.time(7, 15), '07:15'), (datetime.time(8, 15), '08:15')], null=True),
        ),
    ]
