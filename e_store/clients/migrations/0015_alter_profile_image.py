# Generated by Django 4.1.4 on 2023-01-27 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0014_alter_profile_date_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]