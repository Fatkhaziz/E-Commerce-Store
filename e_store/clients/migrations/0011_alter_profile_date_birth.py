# Generated by Django 4.1.4 on 2023-01-24 14:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0010_alter_profile_date_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_birth',
            field=models.DateField(default=datetime.date(2023, 1, 24)),
        ),
    ]
