# Generated by Django 4.1.4 on 2023-01-08 18:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.TextField(default=2, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='insta',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_birth',
            field=models.DateField(default=datetime.date(2023, 1, 9)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='avatar.png', null=True, upload_to=''),
        ),
    ]
