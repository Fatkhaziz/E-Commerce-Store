# Generated by Django 4.1.4 on 2023-01-27 09:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0013_alter_profile_date_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_birth',
            field=models.DateField(default=datetime.date(2023, 1, 27)),
        ),
    ]
